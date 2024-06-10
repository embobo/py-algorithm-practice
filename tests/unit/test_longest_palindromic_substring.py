import pytest

from src.algorithms.longest_palindromic_substring import longest_palindromic_substring


class TestLongestPalindromicSubsring:
    @pytest.mark.parametrize(
        "in_str, expected",
        [
            ("abada", "aba"),
            ("zzz", "zzz"),
            ("cbbd", "bb"),
            ("abcdeffeg", "effe"),
        ],
    )
    def test_longest_palindromic_substring(self, in_str: str, expected: int):
        assert longest_palindromic_substring(in_str) == expected
