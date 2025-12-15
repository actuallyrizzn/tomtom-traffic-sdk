from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import httpx

from .exceptions import ApiError, ValidationError
from .utils import bracket_list, comma_join, drop_none


@dataclass(frozen=True)
class _RequestConfig:
    api_key: str
    base_url: str


class TomTomTrafficClient:
    """Client for TomTom Traffic APIs.

    Covers endpoints documented in `docs/tomtom-traffic-api.md`, including:
    - TomTom Maps endpoints under `/traffic/...`
    - TomTom Orbis Maps endpoints under `/maps/orbis/traffic/...`

    Note: Docs also reference gated Orbis "Extended Tiles" pages; those are not implementable
    from the repository documentation alone.
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = "https://api.tomtom.com",
        timeout: float | None = 10.0,
        http: httpx.Client | None = None,
        raise_for_status: bool = True,
    ) -> None:
        if not api_key:
            raise ValidationError("api_key is required")

        self._cfg = _RequestConfig(api_key=api_key, base_url=base_url.rstrip("/"))
        self._raise_for_status = raise_for_status
        self._owns_http = http is None
        self._http = http or httpx.Client(base_url=self._cfg.base_url, timeout=timeout)

        self.maps = TomTomMapsTrafficAPI(self)
        self.orbis = TomTomOrbisTrafficAPI(self)

    def close(self) -> None:
        if self._owns_http:
            self._http.close()

    def __enter__(self) -> TomTomTrafficClient:
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # type: ignore[override]
        self.close()

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        p = {"key": self._cfg.api_key}
        if params:
            p.update(params)

        resp = self._http.request(method, path, params=p, json=json, headers=headers)
        if self._raise_for_status and resp.status_code >= 400:
            body: str | bytes | None
            try:
                body = resp.text
            except Exception:  # pragma: no cover
                body = resp.content
            raise ApiError(status_code=resp.status_code, message=resp.reason_phrase, body=body)
        return resp


class TomTomMapsTrafficAPI:
    def __init__(self, client: TomTomTrafficClient) -> None:
        self._c = client

    # Traffic Incidents (v5)
    def incident_details(
        self,
        *,
        version: int = 5,
        bbox: tuple[float, float, float, float] | str | None = None,
        ids: list[str] | str | None = None,
        fields: str | None = None,
        language: str | None = None,
        t: str | None = None,
        category_filter: str | None = None,
        time_validity_filter: str | None = None,
    ) -> httpx.Response:
        if (bbox is None) == (ids is None):
            raise ValidationError("exactly one of bbox or ids must be provided")

        q: dict[str, Any] = {
            "fields": fields,
            "language": language,
            "t": t,
            "categoryFilter": category_filter,
            "timeValidityFilter": time_validity_filter,
        }
        if bbox is not None:
            q["bbox"] = comma_join(bbox) if not isinstance(bbox, str) else bbox
        if ids is not None:
            q["ids"] = comma_join(ids) if isinstance(ids, list) else ids

        return self._c._request(
            "GET",
            f"/traffic/services/{version}/incidentDetails",
            params=drop_none(q),
        )

    def incident_details_by_ids(
        self,
        *,
        version: int = 5,
        ids: list[str],
        fields: str | None = None,
        language: str | None = None,
        t: str | None = None,
        category_filter: str | None = None,
        time_validity_filter: str | None = None,
    ) -> httpx.Response:
        if not ids:
            raise ValidationError("ids must be a non-empty list")

        q = drop_none(
            {
                "fields": fields,
                "language": language,
                "t": t,
                "categoryFilter": category_filter,
                "timeValidityFilter": time_validity_filter,
            }
        )
        return self._c._request(
            "POST",
            f"/traffic/services/{version}/incidentDetails",
            params=q,
            json={"ids": ids},
        )

    # Traffic Incidents (deprecated v4 endpoint)
    def incident_details_deprecated(
        self,
        *,
        version: int = 4,
        style: str,
        bounding_box: str,
        zoom: int,
        traffic_model_id: str,
        response_format: str,
        language: str | None = None,
        projection: str | None = None,
        geometries: str | None = None,
        expand_cluster: bool | None = None,
        original_position: bool | None = None,
        jsonp: str | None = None,
    ) -> httpx.Response:
        if not style:
            raise ValidationError("style is required")
        if not bounding_box:
            raise ValidationError("bounding_box is required")
        if not response_format:
            raise ValidationError("response_format is required")

        q = drop_none(
            {
                "language": language,
                "projection": projection,
                "geometries": geometries,
                "expandCluster": expand_cluster,
                "originalPosition": original_position,
                "jsonp": jsonp,
            }
        )
        path = (
            f"/traffic/services/{version}/incidentDetails/"
            f"{style}/{bounding_box}/{zoom}/{traffic_model_id}/{response_format}"
        )
        return self._c._request("GET", path, params=q)

    def incident_viewport(
        self,
        *,
        version: int = 4,
        bounding_box: str,
        bounding_zoom: int,
        overview_box: str,
        overview_zoom: int,
        copyright: bool,
        content_type: str,
        jsonp: str | None = None,
    ) -> httpx.Response:
        q = drop_none({"jsonp": jsonp})
        path = (
            f"/traffic/services/{version}/incidentViewport/"
            f"{bounding_box}/{bounding_zoom}/{overview_box}/{overview_zoom}/{str(copyright).lower()}/{content_type}"
        )
        return self._c._request("GET", path, params=q)

    # Traffic Flow
    def flow_segment_data(
        self,
        *,
        version: int = 4,
        style: str,
        zoom: int,
        response_format: str,
        point: str,
        unit: str | None = None,
        thickness: int | None = None,
        open_lr: bool | None = None,
        jsonp: str | None = None,
    ) -> httpx.Response:
        q = drop_none(
            {
                "point": point,
                "unit": unit,
                "thickness": thickness,
                "openLr": open_lr,
                "jsonp": jsonp,
            }
        )
        path = f"/traffic/services/{version}/flowSegmentData/{style}/{zoom}/{response_format}"
        return self._c._request("GET", path, params=q)

    # Tiles - Incidents
    def raster_incident_tile(
        self,
        *,
        version: int = 4,
        style: str,
        zoom: int,
        x: int,
        y: int,
        image_format: str,
        t: str | None = None,
        tile_size: int | None = None,
    ) -> httpx.Response:
        q = drop_none({"t": t, "tileSize": tile_size})
        path = f"/traffic/map/{version}/tile/incidents/{style}/{zoom}/{x}/{y}.{image_format}"
        return self._c._request("GET", path, params=q)

    def vector_incident_tile(
        self,
        *,
        version: int = 4,
        zoom: int,
        x: int,
        y: int,
        tile_format: str = "pbf",
        t: str | None = None,
        tags: list[str] | str | None = None,
    ) -> httpx.Response:
        q: dict[str, Any] = {"t": t}
        if tags is not None:
            q["tags"] = bracket_list(tags) if isinstance(tags, list) else tags
        path = f"/traffic/map/{version}/tile/incidents/{zoom}/{x}/{y}.{tile_format}"
        return self._c._request("GET", path, params=drop_none(q))

    # Tiles - Flow
    def raster_flow_tile(
        self,
        *,
        version: int = 4,
        style: str,
        zoom: int,
        x: int,
        y: int,
        image_format: str,
        thickness: int | None = None,
        tile_size: int | None = None,
    ) -> httpx.Response:
        q = drop_none({"thickness": thickness, "tileSize": tile_size})
        path = f"/traffic/map/{version}/tile/flow/{style}/{zoom}/{x}/{y}.{image_format}"
        return self._c._request("GET", path, params=q)

    def vector_flow_tile(
        self,
        *,
        version: int = 4,
        flow_type: str,
        zoom: int,
        x: int,
        y: int,
        tile_format: str = "pbf",
        road_types: list[int] | str | None = None,
        traffic_level_step: int | None = None,
        margin: float | None = None,
        tags: list[str] | str | None = None,
    ) -> httpx.Response:
        q: dict[str, Any] = {
            "trafficLevelStep": traffic_level_step,
            "margin": margin,
        }
        if road_types is not None:
            q["roadTypes"] = (
                bracket_list(road_types) if isinstance(road_types, list) else road_types
            )
        if tags is not None:
            q["tags"] = bracket_list(tags) if isinstance(tags, list) else tags
        path = f"/traffic/map/{version}/tile/flow/{flow_type}/{zoom}/{x}/{y}.{tile_format}"
        return self._c._request("GET", path, params=drop_none(q))

    def vector_flow_tile_legacy_base(
        self,
        *,
        version: int = 4,
        flow_type: str,
        zoom: int,
        x: int,
        y: int,
        tile_format: str = "pbf",
    ) -> httpx.Response:
        # The markdown includes example URLs under `/map/{version}/tile/flow/...` (no `/traffic`).
        path = f"/map/{version}/tile/flow/{flow_type}/{zoom}/{x}/{y}.{tile_format}"
        return self._c._request("GET", path)


class TomTomOrbisTrafficAPI:
    def __init__(self, client: TomTomTrafficClient) -> None:
        self._c = client

    def incident_details(
        self,
        *,
        api_version: int = 1,
        bbox: tuple[float, float, float, float] | str | None = None,
        ids: list[str] | str | None = None,
        fields: str | None = None,
        language: str | None = None,
        t: str | None = None,
        category_filter: str | None = None,
        time_validity_filter: str | None = None,
    ) -> httpx.Response:
        if (bbox is None) == (ids is None):
            raise ValidationError("exactly one of bbox or ids must be provided")

        q: dict[str, Any] = {
            "apiVersion": api_version,
            "fields": fields,
            "language": language,
            "t": t,
            "categoryFilter": category_filter,
            "timeValidityFilter": time_validity_filter,
        }
        if bbox is not None:
            q["bbox"] = comma_join(bbox) if not isinstance(bbox, str) else bbox
        if ids is not None:
            q["ids"] = comma_join(ids) if isinstance(ids, list) else ids
        headers = {"TomTom-Api-Version": str(api_version)}
        return self._c._request(
            "GET",
            "/maps/orbis/traffic/incidentDetails",
            params=drop_none(q),
            headers=headers,
        )

    def incident_details_by_ids(
        self,
        *,
        api_version: int = 1,
        ids: list[str],
        fields: str | None = None,
        language: str | None = None,
        t: str | None = None,
        category_filter: str | None = None,
        time_validity_filter: str | None = None,
    ) -> httpx.Response:
        if not ids:
            raise ValidationError("ids must be a non-empty list")

        q = drop_none(
            {
                "apiVersion": api_version,
                "fields": fields,
                "language": language,
                "t": t,
                "categoryFilter": category_filter,
                "timeValidityFilter": time_validity_filter,
            }
        )
        headers = {"TomTom-Api-Version": str(api_version)}
        return self._c._request(
            "POST",
            "/maps/orbis/traffic/incidentDetails",
            params=q,
            json={"ids": ids},
            headers=headers,
        )

    def incident_tile(
        self,
        *,
        api_version: int = 1,
        zoom: int,
        x: int,
        y: int,
        tile_format: str,
        style: str | None = None,
        t: str | None = None,
    ) -> httpx.Response:
        q: dict[str, Any] = {"apiVersion": api_version, "t": t}
        if style is not None:
            q["style"] = style
        headers = {"TomTom-Api-Version": str(api_version)}
        path = f"/maps/orbis/traffic/tile/incidents/{zoom}/{x}/{y}.{tile_format}"
        return self._c._request("GET", path, params=drop_none(q), headers=headers)

    def flow_tile(
        self,
        *,
        api_version: int = 1,
        zoom: int,
        x: int,
        y: int,
        tile_format: str,
        style: str | None = None,
        tile_size: int | None = None,
    ) -> httpx.Response:
        q: dict[str, Any] = {"apiVersion": api_version, "tileSize": tile_size}
        if style is not None:
            q["style"] = style
        headers = {"TomTom-Api-Version": str(api_version)}
        path = f"/maps/orbis/traffic/tile/flow/{zoom}/{x}/{y}.{tile_format}"
        return self._c._request("GET", path, params=drop_none(q), headers=headers)
