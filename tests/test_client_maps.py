import httpx
import pytest
import respx

from tomtom_traffic_sdk import ApiError, TomTomTrafficClient, ValidationError


@respx.mock
def test_maps_incident_details_requires_exactly_one_of_bbox_or_ids() -> None:
    with TomTomTrafficClient("k") as c:
        with pytest.raises(ValidationError):
            c.maps.incident_details()
        with pytest.raises(ValidationError):
            c.maps.incident_details(bbox=(0, 0, 1, 1), ids=["x"])


@respx.mock
def test_maps_incident_details_bbox_builds_query() -> None:
    route = respx.get("https://api.tomtom.com/traffic/services/5/incidentDetails").respond(200, json={"ok": True})

    with TomTomTrafficClient("k") as c:
        r = c.maps.incident_details(
            bbox=(1.1, 2.2, 3.3, 4.4),
            fields="f",
            language="en-GB",
            t="-1",
            category_filter="0,1",
            time_validity_filter="present",
        )

    assert route.called
    req = route.calls.last.request
    assert req.url.params["key"] == "k"
    assert req.url.params["bbox"] == "1.1,2.2,3.3,4.4"
    assert req.url.params["fields"] == "f"
    assert req.url.params["language"] == "en-GB"
    assert req.url.params["t"] == "-1"
    assert req.url.params["categoryFilter"] == "0,1"
    assert req.url.params["timeValidityFilter"] == "present"
    assert r.json() == {"ok": True}


@respx.mock
def test_maps_incident_details_ids_builds_query() -> None:
    route = respx.get("https://api.tomtom.com/traffic/services/5/incidentDetails").respond(200, json={"ok": True})

    with TomTomTrafficClient("k") as c:
        c.maps.incident_details(ids=["a", "b"])

    assert route.called
    req = route.calls.last.request
    assert req.url.params["ids"] == "a,b"


@respx.mock
def test_maps_incident_details_by_ids_post() -> None:
    route = respx.post("https://api.tomtom.com/traffic/services/5/incidentDetails").respond(200, json={"ok": True})

    with TomTomTrafficClient("k") as c:
        c.maps.incident_details_by_ids(ids=["x"])

    assert route.called
    req = route.calls.last.request
    assert req.url.params["key"] == "k"
    assert req.headers.get("content-type", "").startswith("application/json")
    assert req.content == b'{"ids":["x"]}'


@respx.mock
def test_maps_deprecated_incident_details() -> None:
    route = respx.get(
        "https://api.tomtom.com/traffic/services/4/incidentDetails/s3/BOX/11/TMID/xml"
    ).respond(200, text="ok")

    with TomTomTrafficClient("k") as c:
        c.maps.incident_details_deprecated(
            style="s3",
            bounding_box="BOX",
            zoom=11,
            traffic_model_id="TMID",
            response_format="xml",
            expand_cluster=True,
            original_position=False,
        )

    assert route.called
    req = route.calls.last.request
    assert req.url.params["expandCluster"] == "true"
    assert req.url.params["originalPosition"] == "false"


@respx.mock
def test_maps_incident_viewport() -> None:
    route = respx.get(
        "https://api.tomtom.com/traffic/services/4/incidentViewport/BB/2/OB/2/true/json"
    ).respond(200, json={"v": 1})

    with TomTomTrafficClient("k") as c:
        c.maps.incident_viewport(
            bounding_box="BB",
            bounding_zoom=2,
            overview_box="OB",
            overview_zoom=2,
            copyright=True,
            content_type="json",
        )

    assert route.called
    assert route.calls.last.request.url.params["key"] == "k"


@respx.mock
def test_maps_flow_segment_data() -> None:
    route = respx.get("https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml").respond(200, text="x")

    with TomTomTrafficClient("k") as c:
        c.maps.flow_segment_data(style="absolute", zoom=10, response_format="xml", point="52,4")

    assert route.called
    assert route.calls.last.request.url.params["point"] == "52,4"


@respx.mock
def test_maps_raster_incident_tile() -> None:
    route = respx.get("https://api.tomtom.com/traffic/map/4/tile/incidents/s3/12/1/2.png").respond(200, content=b"png")

    with TomTomTrafficClient("k") as c:
        r = c.maps.raster_incident_tile(style="s3", zoom=12, x=1, y=2, image_format="png", t="-1", tile_size=512)

    assert route.called
    assert route.calls.last.request.url.params["t"] == "-1"
    assert route.calls.last.request.url.params["tileSize"] == "512"
    assert r.content == b"png"


@respx.mock
def test_maps_vector_incident_tile_tags() -> None:
    route = respx.get("https://api.tomtom.com/traffic/map/4/tile/incidents/5/4/8.pbf").respond(200, content=b"pbf")

    with TomTomTrafficClient("k") as c:
        c.maps.vector_incident_tile(zoom=5, x=4, y=8, tags=["a", "b"])

    assert route.called
    assert route.calls.last.request.url.params["tags"] == "[a,b]"


@respx.mock
def test_maps_raster_flow_tile() -> None:
    route = respx.get("https://api.tomtom.com/traffic/map/4/tile/flow/absolute/12/1/2.png").respond(200, content=b"x")

    with TomTomTrafficClient("k") as c:
        c.maps.raster_flow_tile(style="absolute", zoom=12, x=1, y=2, image_format="png", thickness=2, tile_size=256)

    assert route.called
    req = route.calls.last.request
    assert req.url.params["thickness"] == "2"
    assert req.url.params["tileSize"] == "256"


@respx.mock
def test_maps_vector_flow_tile() -> None:
    route = respx.get("https://api.tomtom.com/traffic/map/4/tile/flow/relative/5/4/8.pbf").respond(200, content=b"x")

    with TomTomTrafficClient("k") as c:
        c.maps.vector_flow_tile(flow_type="relative", zoom=5, x=4, y=8, road_types=[2, 4, 5], tags=["t1"], margin=0.04)

    assert route.called
    req = route.calls.last.request
    assert req.url.params["roadTypes"] == "[2,4,5]"
    assert req.url.params["tags"] == "[t1]"
    assert req.url.params["margin"] == "0.04"


@respx.mock
def test_maps_vector_flow_tile_legacy_base_path() -> None:
    route = respx.get("https://api.tomtom.com/map/4/tile/flow/absolute/17/64989/42178.pbf").respond(200, content=b"x")

    with TomTomTrafficClient("k") as c:
        c.maps.vector_flow_tile_legacy_base(flow_type="absolute", zoom=17, x=64989, y=42178)

    assert route.called


def test_api_error_when_raise_for_status_is_true() -> None:
    transport = httpx.MockTransport(lambda req: httpx.Response(403, request=req, text="no"))
    http = httpx.Client(base_url="https://api.tomtom.com", transport=transport)

    c = TomTomTrafficClient("k", http=http, raise_for_status=True)
    with pytest.raises(ApiError) as e:
        c.maps.flow_segment_data(style="absolute", zoom=10, response_format="xml", point="52,4")

    assert e.value.status_code == 403


def test_no_raise_for_status_allows_error_response() -> None:
    transport = httpx.MockTransport(lambda req: httpx.Response(403, request=req, text="no"))
    http = httpx.Client(base_url="https://api.tomtom.com", transport=transport)

    c = TomTomTrafficClient("k", http=http, raise_for_status=False)
    r = c.maps.flow_segment_data(style="absolute", zoom=10, response_format="xml", point="52,4")
    assert r.status_code == 403


def test_client_requires_api_key() -> None:
    with pytest.raises(ValidationError):
        TomTomTrafficClient("")


@respx.mock
def test_maps_incident_details_accepts_string_bbox_or_ids() -> None:
    route = respx.get("https://api.tomtom.com/traffic/services/5/incidentDetails").respond(200, json={"ok": True})

    with TomTomTrafficClient("k") as c:
        c.maps.incident_details(bbox="1,2,3,4")
        c.maps.incident_details(ids="a,b")

    assert route.call_count == 2


@respx.mock
def test_maps_incident_details_by_ids_requires_non_empty_ids() -> None:
    with TomTomTrafficClient("k") as c:
        with pytest.raises(ValidationError):
            c.maps.incident_details_by_ids(ids=[])


@respx.mock
def test_maps_deprecated_incident_details_validates_required_fields() -> None:
    with TomTomTrafficClient("k") as c:
        with pytest.raises(ValidationError):
            c.maps.incident_details_deprecated(
                style="",
                bounding_box="BOX",
                zoom=11,
                traffic_model_id="TMID",
                response_format="xml",
            )
        with pytest.raises(ValidationError):
            c.maps.incident_details_deprecated(
                style="s3",
                bounding_box="",
                zoom=11,
                traffic_model_id="TMID",
                response_format="xml",
            )
        with pytest.raises(ValidationError):
            c.maps.incident_details_deprecated(
                style="s3",
                bounding_box="BOX",
                zoom=11,
                traffic_model_id="TMID",
                response_format="",
            )


@respx.mock
def test_maps_vector_incident_tile_tags_as_string_passthrough() -> None:
    route = respx.get("https://api.tomtom.com/traffic/map/4/tile/incidents/5/4/8.pbf").respond(200, content=b"pbf")

    with TomTomTrafficClient("k") as c:
        c.maps.vector_incident_tile(zoom=5, x=4, y=8, tags="[a,b]")

    assert route.called
    assert route.calls.last.request.url.params["tags"] == "[a,b]"


@respx.mock
def test_maps_vector_flow_tile_accepts_string_filters() -> None:
    route = respx.get("https://api.tomtom.com/traffic/map/4/tile/flow/relative/5/4/8.pbf").respond(200, content=b"x")

    with TomTomTrafficClient("k") as c:
        c.maps.vector_flow_tile(flow_type="relative", zoom=5, x=4, y=8, road_types="[2,4]", tags="[t1,t2]")

    assert route.called
    req = route.calls.last.request
    assert req.url.params["roadTypes"] == "[2,4]"
    assert req.url.params["tags"] == "[t1,t2]"


@respx.mock
def test_maps_vector_incident_tile_without_tags_does_not_send_tags_param() -> None:
    route = respx.get("https://api.tomtom.com/traffic/map/4/tile/incidents/5/4/8.pbf").respond(200, content=b"pbf")

    with TomTomTrafficClient("k") as c:
        c.maps.vector_incident_tile(zoom=5, x=4, y=8)

    assert route.called
    assert "tags" not in route.calls.last.request.url.params


@respx.mock
def test_maps_vector_flow_tile_without_optional_filters_sends_no_filter_params() -> None:
    route = respx.get("https://api.tomtom.com/traffic/map/4/tile/flow/relative/5/4/8.pbf").respond(200, content=b"x")

    with TomTomTrafficClient("k") as c:
        c.maps.vector_flow_tile(flow_type="relative", zoom=5, x=4, y=8)

    assert route.called
    req = route.calls.last.request
    assert "roadTypes" not in req.url.params
    assert "tags" not in req.url.params


def test_close_does_not_close_injected_http_client() -> None:
    transport = httpx.MockTransport(lambda req: httpx.Response(200, request=req, text="ok"))
    http = httpx.Client(base_url="https://api.tomtom.com", transport=transport)

    c = TomTomTrafficClient("k", http=http)
    assert http.is_closed is False
    c.close()
    assert http.is_closed is False
