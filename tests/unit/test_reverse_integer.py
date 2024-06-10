import pytest

from src.algorithms.reverse_integer import reverse_integer


class TestCountSubstrings:
    @pytest.mark.parametrize(
        "in_int, expected",
        [(6, 6), (123, 321), (-321, -123), (2147483648, 0)],
    )
    def test_reverse_integer(self, in_int: int, expected: int):
        assert reverse_integer(in_int) == expected
