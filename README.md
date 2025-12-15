# tomtom-traffic-sdk

Python SDK for the TomTom Traffic API, covering:

- **TomTom Maps Traffic API** endpoints under `/traffic/...`
- **TomTom Orbis Maps Traffic API** endpoints under `/maps/orbis/traffic/...`

The SDK is implemented on top of [`httpx`](https://www.python-httpx.org/) and exposes a small, explicit set of methods that map directly to TomTom endpoints.

## Documentation

- `docs/tomtom-traffic-api.md`: generated “single-page” snapshot of the TomTom Traffic API docs (Maps + Orbis variants).
- `docs/spec/tomtom-traffic-api.yml`: downloaded OpenAPI spec used as a source input for the snapshot.
- `docs/README.md`: how the docs in `docs/` are organized (and what is generated vs handwritten).

## Requirements

- Python **3.12+**

## Install

This repository is a Python package. For local development:

```bash
python3 -m pip install -e ".[dev]"
```

To install without development tooling:

```bash
python3 -m pip install .
```

## Authentication

TomTom Traffic APIs use an **API key** provided via the query string as `key=...`.

The SDK expects you to pass the key explicitly:

```python
from tomtom_traffic_sdk import TomTomTrafficClient

client = TomTomTrafficClient(api_key="YOUR_TOMTOM_API_KEY")
```

## Quickstart

```python
from tomtom_traffic_sdk import TomTomTrafficClient

with TomTomTrafficClient(api_key="YOUR_TOMTOM_API_KEY") as client:
    # TomTom Maps (Traffic API) - incidentDetails v5 (GET)
    resp = client.maps.incident_details(
        bbox=(4.88, 52.36, 4.89, 52.37),
        language="en-GB",
        t="-1",
    )
    incidents = resp.json()

    # TomTom Maps (Traffic API) - incidentDetails v5 (POST)
    resp2 = client.maps.incident_details_by_ids(ids=["INCIDENT_ID_1"])
    incidents2 = resp2.json()

    # TomTom Orbis Maps - raster incident tile (PNG)
    tile = client.orbis.incident_tile(
        zoom=12,
        x=2044,
        y=1360,
        tile_format="png",
        style="light",
        t="-1",
    )
    png_bytes = tile.content
```

## API surface

The main entry point is `TomTomTrafficClient`, which exposes two sub-clients:

- `client.maps`: TomTom Maps Traffic endpoints (`/traffic/...`)
- `client.orbis`: TomTom Orbis Traffic endpoints (`/maps/orbis/traffic/...`)

### TomTom Maps (`client.maps`)

- `incident_details(...)`: `/traffic/services/{version}/incidentDetails` (GET, v5)
- `incident_details_by_ids(...)`: `/traffic/services/{version}/incidentDetails` (POST, v5)
- `incident_details_deprecated(...)`: `/traffic/services/{version}/incidentDetails/{style}/{boundingBox}/{zoom}/{trafficModelID}/{format}` (GET, v4)
- `incident_viewport(...)`: `/traffic/services/{version}/incidentViewport/...` (GET, v4)
- `flow_segment_data(...)`: `/traffic/services/{version}/flowSegmentData/{style}/{zoom}/{format}` (GET, v4)
- `raster_incident_tile(...)`: `/traffic/map/{version}/tile/incidents/{style}/{zoom}/{x}/{y}.{format}` (GET, v4)
- `vector_incident_tile(...)`: `/traffic/map/{version}/tile/incidents/{zoom}/{x}/{y}.{format}` (GET, v4)
- `raster_flow_tile(...)`: `/traffic/map/{version}/tile/flow/{style}/{zoom}/{x}/{y}.{format}` (GET, v4)
- `vector_flow_tile(...)`: `/traffic/map/{version}/tile/flow/{type}/{zoom}/{x}/{y}.{format}` (GET, v4)
- `vector_flow_tile_legacy_base(...)`: `/map/{version}/tile/flow/{type}/{zoom}/{x}/{y}.{format}` (GET, legacy base path seen in docs)

### TomTom Orbis (`client.orbis`)

- `incident_details(...)`: `/maps/orbis/traffic/incidentDetails` (GET)
- `incident_details_by_ids(...)`: `/maps/orbis/traffic/incidentDetails` (POST)
- `incident_tile(...)`: `/maps/orbis/traffic/tile/incidents/{zoom}/{x}/{y}.{format}` (GET)
- `flow_tile(...)`: `/maps/orbis/traffic/tile/flow/{zoom}/{x}/{y}.{format}` (GET)

## Error handling

By default, the client raises on non-2xx responses:

- `tomtom_traffic_sdk.exceptions.ValidationError`: invalid SDK inputs (missing required args, mutually-exclusive params, etc.)
- `tomtom_traffic_sdk.exceptions.ApiError`: HTTP error responses when `raise_for_status=True`

If you want to handle HTTP error responses yourself, disable raising:

```python
from tomtom_traffic_sdk import TomTomTrafficClient

client = TomTomTrafficClient(api_key="YOUR_TOMTOM_API_KEY", raise_for_status=False)
resp = client.maps.flow_segment_data(style="relative0", zoom=10, response_format="json", point="52.41072,4.84239")
if resp.status_code >= 400:
    print(resp.status_code, resp.text)
```

## HTTP configuration

You can control the base URL and timeouts, or provide your own `httpx.Client`:

```python
import httpx
from tomtom_traffic_sdk import TomTomTrafficClient

http = httpx.Client(timeout=20.0)
client = TomTomTrafficClient(api_key="YOUR_TOMTOM_API_KEY", http=http, base_url="https://api.tomtom.com")
```

## Development

Install dev dependencies:

```bash
python3 -m pip install -e ".[dev]"
```

Run tests (coverage is configured to fail below 100%):

```bash
python3 -m pytest
```

## License

- **Code** (everything under `src/` and `tests/`): **GNU Affero General Public License v3.0 only** (AGPL-3.0-only). See `LICENSE`.
- **Non-code content** (docs, prose, etc.): **Creative Commons Attribution-ShareAlike 4.0 International** (CC BY-SA 4.0). See `LICENSES/CC-BY-SA-4.0.txt`.

Third-party content (including TomTom documentation and the downloaded OpenAPI spec) may be subject to additional terms; see `NOTICE`.