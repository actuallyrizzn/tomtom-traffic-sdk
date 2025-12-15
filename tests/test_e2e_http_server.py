from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

import httpx

from tomtom_traffic_sdk import TomTomTrafficClient


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        assert qs.get("key") == ["k"]

        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"path": parsed.path}).encode("utf-8"))

    def log_message(self, format: str, *args) -> None:  # noqa: A002
        # Silence server logs in tests.
        return


def test_real_http_round_trip_against_local_server() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 0), _Handler)
    host, port = server.server_address

    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()

    try:
        base_url = f"http://{host}:{port}"
        with TomTomTrafficClient("k", base_url=base_url) as c:
            r = c.maps.flow_segment_data(style="absolute", zoom=10, response_format="xml", point="52,4")
            assert r.status_code == 200
            assert r.json()["path"].endswith("/traffic/services/4/flowSegmentData/absolute/10/xml")
    finally:
        server.shutdown()
        server.server_close()
        t.join(timeout=2)


def test_can_inject_httpx_client() -> None:
    transport = httpx.MockTransport(lambda req: httpx.Response(200, request=req, json={"ok": True}))
    http = httpx.Client(base_url="https://api.tomtom.com", transport=transport)

    c = TomTomTrafficClient("k", http=http)
    r = c.maps.incident_details(ids=["x"])
    assert r.json() == {"ok": True}
