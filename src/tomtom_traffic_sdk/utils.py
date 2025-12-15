from __future__ import annotations

from collections.abc import Iterable, Mapping


def comma_join(values: Iterable[object]) -> str:
    return ",".join(str(v) for v in values)


def bracket_list(values: Iterable[object]) -> str:
    # TomTom vector-tile APIs document lists as: [a,b,c] or [2,4,5]
    return "[" + ",".join(str(v) for v in values) + "]"


def drop_none(d: Mapping[str, object | None]) -> dict[str, object]:
    return {k: v for k, v in d.items() if v is not None}
