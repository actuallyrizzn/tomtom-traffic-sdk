import pytest
import respx

from tomtom_traffic_sdk import TomTomTrafficClient, ValidationError


@respx.mock
def test_orbis_incident_details_sets_api_version_query_and_header() -> None:
    route = respx.get("https://api.tomtom.com/maps/orbis/traffic/incidentDetails").respond(200, json={"ok": True})

    with TomTomTrafficClient("k") as c:
        c.orbis.incident_details(api_version=1, bbox=(1, 2, 3, 4))

    assert route.called
    req = route.calls.last.request
    assert req.url.params["apiVersion"] == "1"
    assert req.headers["TomTom-Api-Version"] == "1"


@respx.mock
def test_orbis_incident_details_by_ids_post() -> None:
    route = respx.post("https://api.tomtom.com/maps/orbis/traffic/incidentDetails").respond(200, json={"ok": True})

    with TomTomTrafficClient("k") as c:
        c.orbis.incident_details_by_ids(api_version=1, ids=["x"], fields="f")

    assert route.called
    req = route.calls.last.request
    assert req.url.params["apiVersion"] == "1"
    assert req.url.params["fields"] == "f"
    assert req.headers["TomTom-Api-Version"] == "1"


@respx.mock
def test_orbis_incident_tile_optional_style_and_t() -> None:
    route = respx.get("https://api.tomtom.com/maps/orbis/traffic/tile/incidents/12/2044/1360.png").respond(200, content=b"x")

    with TomTomTrafficClient("k") as c:
        c.orbis.incident_tile(api_version=1, zoom=12, x=2044, y=1360, tile_format="png", style="light", t="-1")

    assert route.called
    req = route.calls.last.request
    assert req.url.params["style"] == "light"
    assert req.url.params["t"] == "-1"


@respx.mock
def test_orbis_flow_tile_style_and_tile_size() -> None:
    route = respx.get("https://api.tomtom.com/maps/orbis/traffic/tile/flow/12/2044/1360.png").respond(200, content=b"x")

    with TomTomTrafficClient("k") as c:
        c.orbis.flow_tile(api_version=1, zoom=12, x=2044, y=1360, tile_format="png", style="dark", tile_size=512)

    assert route.called
    req = route.calls.last.request
    assert req.url.params["style"] == "dark"
    assert req.url.params["tileSize"] == "512"


@respx.mock
def test_orbis_incident_details_validates_mutual_exclusion() -> None:
    with TomTomTrafficClient("k") as c:
        with pytest.raises(ValidationError):
            c.orbis.incident_details()
        with pytest.raises(ValidationError):
            c.orbis.incident_details(bbox=(1, 2, 3, 4), ids=["x"])


@respx.mock
def test_orbis_incident_details_accepts_string_bbox_or_ids() -> None:
    route = respx.get("https://api.tomtom.com/maps/orbis/traffic/incidentDetails").respond(200, json={"ok": True})

    with TomTomTrafficClient("k") as c:
        c.orbis.incident_details(api_version=1, bbox="1,2,3,4")
        c.orbis.incident_details(api_version=1, ids="a,b")

    assert route.call_count == 2


@respx.mock
def test_orbis_incident_details_by_ids_requires_non_empty_ids() -> None:
    with TomTomTrafficClient("k") as c:
        with pytest.raises(ValidationError):
            c.orbis.incident_details_by_ids(api_version=1, ids=[])


@respx.mock
def test_orbis_tiles_without_optional_style() -> None:
    incident = respx.get("https://api.tomtom.com/maps/orbis/traffic/tile/incidents/5/4/8.pbf").respond(200, content=b"x")
    flow = respx.get("https://api.tomtom.com/maps/orbis/traffic/tile/flow/5/4/8.pbf").respond(200, content=b"x")

    with TomTomTrafficClient("k") as c:
        c.orbis.incident_tile(api_version=1, zoom=5, x=4, y=8, tile_format="pbf")
        c.orbis.flow_tile(api_version=1, zoom=5, x=4, y=8, tile_format="pbf")

    assert incident.called
    assert "style" not in incident.calls.last.request.url.params
    assert flow.called
    assert "style" not in flow.calls.last.request.url.params
