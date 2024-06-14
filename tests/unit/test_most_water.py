from typing import List

import pytest

from src.algorithms.most_water import max_area


class TestLongestPalindromicSubsring:
    @pytest.mark.parametrize(
        "input, expected",
        [
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
            ([8, 0, 0, 0, 9], 32),
            ([0, 1, 15, 10, 1], 10),
        ],
    )
    def test_longest_palindromic_substring(self, input: List[int], expected: int):
        assert max_area(input) == expected
