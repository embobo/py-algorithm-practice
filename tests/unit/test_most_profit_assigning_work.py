from typing import List

import pytest

from src.algorithms.most_profit_assigning_work import most_profit


class TestMostProfitAssigningWork:
    @pytest.mark.parametrize(
        "difficulty, profit, worker, expected",
        [
            ([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7], 100),
            ([85, 47, 57], [24, 66, 99], [40, 25, 25], 0),
        ],
    )
    def test_most_profit(
        self, difficulty: List[int], profit: List[int], worker: List[int], expected: int
    ):
        assert most_profit(difficulty, profit, worker) == expected
