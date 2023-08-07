import pytest


from utils.arrs import get, my_slice


@pytest.mark.parametrize("array, index, default, expected", [
    ([1, 2, 3], 2, "test", 3),
     ([], -1, "test", "test"),
])
def test_get(array, index, default, expected):
    assert get(array, index, default) == expected


@pytest.mark.parametrize("coll, start, end, expen", [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([], 1, None, []),
    ([1, 2, 3], -1, None, [3]),
([1, 2, 3], -4, None, [1, 2, 3])
])
def test_slice(coll, start, end, expen):
    assert my_slice(coll, start, end) == expen
    # assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
