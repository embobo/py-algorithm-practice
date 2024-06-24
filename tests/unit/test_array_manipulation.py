from src.algorithms.array_manipulation import array_manipulation


class TestArrayManipulation:
    def test_case_2(self, hackerrank_array_manipulation_case_2: str):
        expected: int = 31
        assert array_manipulation(hackerrank_array_manipulation_case_2) == expected

    def test_case_7(self, hackerrank_array_manipulation_case_7: str):
        expected: int = 2497169732
        assert array_manipulation(hackerrank_array_manipulation_case_7) == expected
