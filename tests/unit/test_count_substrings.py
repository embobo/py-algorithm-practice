import pytest

from src.algorithms.count_substrings import count_substrings_bounded_by


class TestCountSubstrings:
    @pytest.mark.parametrize(
        "in_str, c, expected",
        [
            ("abada", "a", 6),
            ("zzz", "z", 6),
            ("ababa", "b", 3),
            ("avadakadabra", "a", 21),
        ],
    )
    def test_count_start_end_with_char(self, in_str: str, c: str, expected: int):
        assert count_substrings_bounded_by(in_str, c) == expected
