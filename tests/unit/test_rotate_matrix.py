from typing import List

import pytest

from src.algorithms.rotate_matrix import rotate_matrix


class TestRotateMatrix:
    @pytest.mark.parametrize(
        "input, expected",
        [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]])],
    )
    def test_rotate_matrix(self, input: List[List[int]], expected: List[List[int]]):
        rotate_matrix(input)
        assert input == expected
