# tomtom-traffic-sdk

## Docs

- `docs/tomtom-traffic-api.md`: Aggregated Traffic API reference (TomTom Maps + TomTom Orbis Maps).
- `docs/spec/tomtom-traffic-api.yml`: Downloaded OpenAPI spec used as a source input.

## Python SDK

### Install (dev)

```bash
python3 -m pip install -e ".[dev]"
```

### Usage

```python
from tomtom_traffic_sdk import TomTomTrafficClient

with TomTomTrafficClient(api_key="YOUR_KEY") as client:
    # TomTom Maps (Traffic API)
    resp = client.maps.incident_details(
        bbox=(4.88, 52.36, 4.89, 52.37),
        language="en-GB",
        t="-1",
    )
    incidents = resp.json()

    # TomTom Orbis Maps
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

### Tests + coverage

```bash
python3 -m pytest
```