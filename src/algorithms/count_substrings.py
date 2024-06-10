"""
Leetcode
ref: https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/description/  # noqa: E501

You are given a string s and a character c. Return the total number of
substrings of s that start and end with c.
"""


def count_substrings_bounded_by(s: str, c: str) -> int:
    n = s.count(c)
    return (n * (n + 1)) / 2
