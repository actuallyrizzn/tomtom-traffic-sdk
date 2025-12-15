#!/usr/bin/env python3
"""
Generates /docs/tomtom-traffic-api.md by scraping TomTom's Developer Portal HTML.

Source of truth pages are under:
  https://developer.tomtom.com/traffic-api/documentation/
"""

from __future__ import annotations

import html
import re
import sys
import textwrap
import urllib.request
from dataclasses import dataclass
from typing import Iterable, List, Optional, Tuple

from bs4 import BeautifulSoup, Tag


BASE = "https://developer.tomtom.com"


TOMTOM_MAPS_ENDPOINT_PAGES = [
    "/traffic-api/documentation/tomtom-maps/traffic-incidents/incident-details",
    "/traffic-api/documentation/tomtom-maps/traffic-incidents/incident-details-deprecated",
    "/traffic-api/documentation/tomtom-maps/traffic-incidents/incident-viewport",
    "/traffic-api/documentation/tomtom-maps/traffic-incidents/raster-incident-tiles",
    "/traffic-api/documentation/tomtom-maps/traffic-incidents/vector-incident-tiles",
    "/traffic-api/documentation/tomtom-maps/traffic-flow/flow-segment-data",
    "/traffic-api/documentation/tomtom-maps/traffic-flow/raster-flow-tiles",
    "/traffic-api/documentation/tomtom-maps/traffic-flow/vector-flow-tiles",
]

TOMTOM_ORBIS_MAPS_ENDPOINT_PAGES = [
    "/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/incident-details",
    "/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/incident-details-v2",
    "/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/raster-incident-tiles",
    "/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/raster-incident-tiles-v2",
    "/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/vector-incident-tiles",
    "/traffic-api/documentation/tomtom-orbis-maps/traffic-incidents/vector-incident-tiles-v2",
    "/traffic-api/documentation/tomtom-orbis-maps/extended/traffic-incidents-extended-tiles",
    "/traffic-api/documentation/tomtom-orbis-maps/traffic-flow/raster-flow-tiles",
    "/traffic-api/documentation/tomtom-orbis-maps/traffic-flow/raster-flow-tiles-v2",
    "/traffic-api/documentation/tomtom-orbis-maps/traffic-flow/vector-flow-tiles",
    "/traffic-api/documentation/tomtom-orbis-maps/traffic-flow/vector-flow-tiles-v2",
    "/traffic-api/documentation/tomtom-orbis-maps/extended/traffic-flow-extended-tiles",
]


def fetch(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "tomtom-traffic-sdk-docs-bot/1.0 (+https://github.com/actuallyrizzn/tomtom-traffic-sdk)",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def _heading_level(tag: Tag) -> Optional[int]:
    if not isinstance(tag, Tag):
        return None
    if tag.name and re.fullmatch(r"h[1-6]", tag.name):
        return int(tag.name[1])
    return None


def _iter_after(start: Tag) -> Iterable[Tag]:
    # Iterate forward in document order.
    cur = start
    while True:
        cur = cur.find_next()
        if cur is None:
            return
        if isinstance(cur, Tag):
            yield cur


def _section_nodes_by_id(soup: BeautifulSoup, heading_id: str) -> List[Tag]:
    h = soup.find(id=heading_id)
    if not isinstance(h, Tag):
        return []
    level = _heading_level(h) or 6
    out: List[Tag] = []
    for node in _iter_after(h):
        node_level = _heading_level(node)
        if node_level is not None and node_level <= level:
            break
        out.append(node)
    return out


def _text(el: Tag) -> str:
    return " ".join(el.get_text(" ", strip=True).split())


def _md_escape(s: str) -> str:
    return s.replace("|", "\\|")


def _table_to_md(table: Tag) -> str:
    rows = []
    for tr in table.find_all("tr"):
        cells = [c.get_text(" ", strip=True) for c in tr.find_all(["th", "td"])]
        if cells:
            rows.append(cells)

    if not rows:
        return ""

    # Normalize width.
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]

    header = rows[0]
    body = rows[1:] if len(rows) > 1 else []

    md = []
    md.append("| " + " | ".join(_md_escape(h) for h in header) + " |")
    md.append("| " + " | ".join(["---"] * width) + " |")
    for r in body:
        md.append("| " + " | ".join(_md_escape(c) for c in r) + " |")
    return "\n".join(md)


@dataclass(frozen=True)
class CodeBlock:
    title: str
    method: Optional[str]
    content: str


def _extract_code_blocks(soup: BeautifulSoup) -> List[CodeBlock]:
    blocks: List[CodeBlock] = []
    for prism in soup.find_all("div", class_=re.compile(r"\bprism-code\b")):
        title_el = prism.find("div", class_=re.compile(r"\bp-title-3-bold\b"))
        if not isinstance(title_el, Tag):
            continue
        title = _text(title_el)

        method = None
        method_el = prism.find("div", class_=re.compile(r"\bp-uppercase\b"))
        if isinstance(method_el, Tag):
            m = _text(method_el)
            if m.lower() in {"get", "post", "put", "delete", "patch"}:
                method = m.lower()

        textarea = prism.find("textarea")
        if not isinstance(textarea, Tag):
            continue

        raw = textarea.get_text()
        raw = html.unescape(raw)
        raw = raw.replace("\r\n", "\n").strip("\n")
        if not raw.strip():
            continue
        blocks.append(CodeBlock(title=title, method=method, content=raw))

    # De-dup by (title, method, content)
    seen = set()
    out: List[CodeBlock] = []
    for b in blocks:
        key = (b.title, b.method, b.content)
        if key in seen:
            continue
        seen.add(key)
        out.append(b)
    return out


def _extract_tables_for_sections(soup: BeautifulSoup, section_ids: List[str]) -> List[Tuple[str, str]]:
    """
    Returns list of (section_title, markdown_table).
    section_title is the heading text for the given id.
    """
    out: List[Tuple[str, str]] = []
    for sid in section_ids:
        heading = soup.find(id=sid)
        if not isinstance(heading, Tag):
            continue
        title = _text(heading)
        nodes = _section_nodes_by_id(soup, sid)
        tables = [n for n in nodes if isinstance(n, Tag) and n.name == "table"]
        for t in tables:
            md = _table_to_md(t)
            if md.strip():
                out.append((title, md))
    return out


def scrape_page(path: str) -> str:
    url = BASE + path
    html_text = fetch(url)
    soup = BeautifulSoup(html_text, "lxml")

    h1 = soup.find("h1")
    title = _text(h1) if isinstance(h1, Tag) else path

    code_blocks = _extract_code_blocks(soup)
    tables = _extract_tables_for_sections(
        soup,
        section_ids=[
            "request-parameters",
            "request-headers",
            "post-request-body",
            "response-data",
            "response-schema",
            "response-field-structure",
            "successful-response",
            "error-response",
        ],
    )

    # Build Markdown
    md: List[str] = []
    md.append(f"### {title}")
    md.append("")
    md.append(f"- **Source**: `{url}`")
    md.append("")

    # Tables (parameters, schema, etc.)
    if tables:
        md.append("#### Tables")
        md.append("")
        for section_title, table_md in tables:
            md.append(f"**{section_title}**")
            md.append("")
            md.append(table_md)
            md.append("")

    # Code blocks (URLs, examples, responses)
    if code_blocks:
        md.append("#### Examples & payloads")
        md.append("")
        for b in code_blocks:
            prefix = f"{b.method.upper()} " if b.method else ""
            md.append(f"**{prefix}{b.title}**")
            md.append("")
            fence = "json" if b.content.lstrip().startswith("{") else "text"
            if b.content.lstrip().startswith("<"):
                fence = "xml"
            md.append(f"```{fence}")
            md.append(b.content)
            md.append("```")
            md.append("")

    return "\n".join(md).rstrip() + "\n"


def main() -> int:
    out_path = "/workspace/docs/tomtom-traffic-api.md"

    doc: List[str] = []
    doc.append("## TomTom Traffic API (docs snapshot)")
    doc.append("")
    doc.append(
        textwrap.dedent(
            """\
            This document is a **generated** aggregation of the TomTom Developer Portal Traffic API documentation pages
            (TomTom Maps + TomTom Orbis Maps variants). It is intended to provide a single place that lists **all endpoints**,
            **all parameters**, and **response formats/examples**.

            - **Base URL**: `https://api.tomtom.com`
            - **Authentication**: API key in query string (`key=...`)
            - **OpenAPI (downloaded)**: `docs/spec/tomtom-traffic-api.yml` (source: `https://developer.tomtom.com/documentation-assets/traffic_22072021_1.yml`)
            - **Official product entry points**:
              - `https://developer.tomtom.com/traffic-api`
              - `https://developer.tomtom.com/traffic-api/api-explorer`
            """
        ).rstrip()
    )
    doc.append("")

    doc.append("### Coverage")
    doc.append("")
    doc.append("#### TomTom Maps")
    doc.append("")
    for p in TOMTOM_MAPS_ENDPOINT_PAGES:
        doc.append(f"- `{BASE}{p}`")
    doc.append("")
    doc.append("#### TomTom Orbis Maps")
    doc.append("")
    for p in TOMTOM_ORBIS_MAPS_ENDPOINT_PAGES:
        doc.append(f"- `{BASE}{p}`")
    doc.append("")

    doc.append("## TomTom Maps endpoints")
    doc.append("")
    for p in TOMTOM_MAPS_ENDPOINT_PAGES:
        doc.append(scrape_page(p))

    doc.append("## TomTom Orbis Maps endpoints")
    doc.append("")
    for p in TOMTOM_ORBIS_MAPS_ENDPOINT_PAGES:
        doc.append(scrape_page(p))

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(doc).rstrip() + "\n")

    print(f"Wrote {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

