"""
Given a string s, return the longest palindromic substring in s.


Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


def _is_palindrome(s: str) -> bool:
    # is a palindrome if the word is the same forwards and backwards
    return s == s[::-1]


def longest_palindromic_substring(s: str) -> str:
    # range, but then invert so we start with the largest length
    # this will allow us to return the largest palindrome as soon as we hit it
    for l in list(range(1, len(s) + 1))[::-1]:  # noqa E741
        # l is the word length to seek in this iteration.
        # This ranges from smallest 1 to the entire word. (reversed to search largest->smallest)
        for idx in range(0, (len(s) - l) + 1):
            # select indices from 0 to len(s) minus the chunk size we're looking at
            word = s[idx : (idx + l)]  # noqa E203
            if _is_palindrome(word):
                return word
