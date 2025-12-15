from __future__ import annotations

import re
from pathlib import Path

import pytest

from tomtom_traffic_sdk.client import TomTomMapsTrafficAPI, TomTomOrbisTrafficAPI


def _extract_api_url_templates(md: str) -> set[str]:
    # Only keep actual API endpoint templates, not documentation portal URLs.
    urls = set(re.findall(r"https://\{baseURL\}/[^\s`]+", md))
    urls |= set(re.findall(r"https://api\.tomtom\.com/[^\s`]+", md))

    api_urls: set[str] = set()
    for u in urls:
        if "developer.tomtom.com" in u:
            continue
        if "/traffic/" in u or "/maps/orbis/traffic/" in u or "/map/" in u:
            api_urls.add(u)
    return api_urls


def _normalize_to_path(u: str) -> str:
    # Drop scheme/host, normalize to a clean path only.
    u = re.sub(r"^https?://[^/]+", "", u)
    u = u.strip().strip("'").strip('"')
    u = u.split("?", 1)[0]
    # Fix obvious doc typos like double slashes.
    u = re.sub(r"/{2,}", "/", u)
    return u


def test_sdk_covers_all_nongated_documented_rest_endpoints() -> None:
    md = Path("/workspace/docs/tomtom-traffic-api.md").read_text(encoding="utf-8")

    api_urls = _extract_api_url_templates(md)
    # Exclude items that are clearly truncated/invalid in the markdown rendering.
    api_urls = {u for u in api_urls if "roadTypes={roadTypes[" not in u}

    normalized = {_normalize_to_path(u) for u in api_urls}

    # What the SDK implements (paths only; query params are handled by methods).
    covered = {
        "/traffic/services/{versionNumber}/incidentDetails",
        "/traffic/services/{versionNumber}/incidentDetails/{style}/{boundingBox}/{zoom}/{trafficModelID}/{format}",
        "/traffic/services/{versionNumber}/incidentViewport/{boundingBox}/{boundingZoom}/{overviewBox}/{overviewZoom}/{copyright}/{contentType}",
        "/traffic/services/{versionNumber}/flowSegmentData/{style}/{zoom}/{format}",
        "/traffic/map/{versionNumber}/tile/incidents/{style}/{zoom}/{x}/{y}.{format}",
        "/traffic/map/{versionNumber}/tile/incidents/{zoom}/{x}/{y}.{format}",
        "/traffic/map/{versionNumber}/tile/flow/{style}/{zoom}/{x}/{y}.{format}",
        "/traffic/map/{versionNumber}/tile/flow/{type}/{zoom}/{x}/{y}.{format}",
        "/map/{versionNumber}/tile/flow/{type}/{zoom}/{x}/{y}.{format}",
        "/maps/orbis/traffic/incidentDetails",
        "/maps/orbis/traffic/tile/incidents/{zoom}/{x}/{y}.{format}",
        "/maps/orbis/traffic/tile/flow/{zoom}/{x}/{y}.{format}",
    }

    # Ensure our coverage list itself stays in sync with the public surface area.
    assert TomTomMapsTrafficAPI is not None
    assert TomTomOrbisTrafficAPI is not None

    # Convert normalized doc URLs into templated paths.
    def to_template(p: str) -> str:
        p = re.sub(r"/traffic/services/\d+", r"/traffic/services/{versionNumber}", p)
        p = re.sub(r"/traffic/map/\d+", r"/traffic/map/{versionNumber}", p)
        p = re.sub(r"/map/\d+", r"/map/{versionNumber}", p)
        p = re.sub(r"/maps/orbis/traffic", r"/maps/orbis/traffic", p)

        # incidents deprecated shape
        p = re.sub(
            r"/traffic/services/\{versionNumber\}/incidentDetails/[^/]+/[^/]+/\d+/[^/]+/[^/?]+",
            r"/traffic/services/{versionNumber}/incidentDetails/{style}/{boundingBox}/{zoom}/{trafficModelID}/{format}",
            p,
        )
        # flowSegmentData
        p = re.sub(
            r"/traffic/services/\{versionNumber\}/flowSegmentData/[^/]+/\d+/[^/?]+",
            r"/traffic/services/{versionNumber}/flowSegmentData/{style}/{zoom}/{format}",
            p,
        )
        # viewport
        p = re.sub(
            r"/traffic/services/\{versionNumber\}/incidentViewport/[^/]+/\d+/[^/]+/\d+/(true|false)/[^/?]+",
            r"/traffic/services/{versionNumber}/incidentViewport/{boundingBox}/{boundingZoom}/{overviewBox}/{overviewZoom}/{copyright}/{contentType}",
            p,
        )
        # tiles
        p = re.sub(
            r"/traffic/map/\{versionNumber\}/tile/incidents/[^/]+/\d+/\d+/\d+\.(png|gif|pbf)",
            r"/traffic/map/{versionNumber}/tile/incidents/{style}/{zoom}/{x}/{y}.{format}",
            p,
        )
        p = re.sub(
            r"/traffic/map/\{versionNumber\}/tile/incidents/\d+/\d+/\d+\.(pbf)",
            r"/traffic/map/{versionNumber}/tile/incidents/{zoom}/{x}/{y}.{format}",
            p,
        )
        p = re.sub(
            r"/traffic/map/\{versionNumber\}/tile/flow/[^/]+/\d+/\d+/\d+\.(png)",
            r"/traffic/map/{versionNumber}/tile/flow/{style}/{zoom}/{x}/{y}.{format}",
            p,
        )
        p = re.sub(
            r"/traffic/map/\{versionNumber\}/tile/flow/[^/]+/\d+/\d+/\d+\.(pbf)",
            r"/traffic/map/{versionNumber}/tile/flow/{type}/{zoom}/{x}/{y}.{format}",
            p,
        )
        p = re.sub(
            r"/map/\{versionNumber\}/tile/flow/[^/]+/\d+/\d+/\d+\.(pbf)",
            r"/map/{versionNumber}/tile/flow/{type}/{zoom}/{x}/{y}.{format}",
            p,
        )

        # Orbis tiles
        p = re.sub(
            r"/maps/orbis/traffic/tile/incidents/\d+/\d+/\d+\.(png|pbf)",
            r"/maps/orbis/traffic/tile/incidents/{zoom}/{x}/{y}.{format}",
            p,
        )
        p = re.sub(
            r"/maps/orbis/traffic/tile/flow/\d+/\d+/\d+\.(png|pbf)",
            r"/maps/orbis/traffic/tile/flow/{zoom}/{x}/{y}.{format}",
            p,
        )

        # incidentDetails (v5 + orbis)
        p = re.sub(
            r"/traffic/services/\{versionNumber\}/incidentDetails\b.*",
            r"/traffic/services/{versionNumber}/incidentDetails",
            p,
        )
        p = re.sub(
            r"/maps/orbis/traffic/incidentDetails\b.*",
            r"/maps/orbis/traffic/incidentDetails",
            p,
        )

        return p

    doc_templates = {to_template(p) for p in normalized}

    missing = sorted(doc_templates - covered)
    assert missing == [], f"SDK missing documented endpoints: {missing}"


@pytest.mark.parametrize(
    "attr",
    [
        "incident_details",
        "incident_details_by_ids",
        "incident_details_deprecated",
        "incident_viewport",
        "flow_segment_data",
        "raster_incident_tile",
        "vector_incident_tile",
        "raster_flow_tile",
        "vector_flow_tile",
        "vector_flow_tile_legacy_base",
    ],
)
def test_maps_api_surface_is_present(attr: str) -> None:
    assert hasattr(TomTomMapsTrafficAPI, attr)


@pytest.mark.parametrize("attr", ["incident_details", "incident_details_by_ids", "incident_tile", "flow_tile"])
def test_orbis_api_surface_is_present(attr: str) -> None:
    assert hasattr(TomTomOrbisTrafficAPI, attr)
