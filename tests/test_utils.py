from tomtom_traffic_sdk.utils import bracket_list, comma_join, drop_none


def test_comma_join() -> None:
    assert comma_join([1, 2, 3]) == "1,2,3"


def test_bracket_list() -> None:
    assert bracket_list(["a", "b"]) == "[a,b]"


def test_drop_none() -> None:
    assert drop_none({"a": 1, "b": None}) == {"a": 1}
