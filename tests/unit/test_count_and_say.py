import pytest

from src.algorithms.count_and_say import count_and_say


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, "1"),
        (2, "11"),
        (3, "21"),
        (4, "1211"),
        (9, "31131211131221"),
        (
            17,
            "11131221131211132221232112111312212321123113112221121113122113111231133221121321132132211331121321231231121113122113322113111221131221",  # noqa: E501
        ),
    ],
)
def test_count_and_say(n: int, expected: str):
    assert count_and_say(n) == expected


@pytest.mark.parametrize("n", [(-1), (31)])
def test_n_within_bounds(n):
    with pytest.raises(ValueError):
        count_and_say(n)
