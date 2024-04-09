"""
LeetCode prompt
ref: https://leetcode.com/problems/count-and-say/description/

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then
converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that
each substring contains exactly one unique digit. Then for each substring, say the number of
digits, then say the digit. Finally, concatenate every said digit.

Example:
    Input: n = 4
    Output: "1211"
    Explanation:
    countAndSay(1) = "1"
    countAndSay(2) = say "1" = one 1 = "11"
    countAndSay(3) = say "11" = two 1's = "21"
    countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

"""


def _say(digits: str) -> str:
    """
    say "1" -> one 1 -> "11"
    say "11" -> two 1s -> "21"
    """
    string = ""
    last = digits[0]
    count = 1
    for c in digits[1:]:
        if c != last:
            string += "{}{}".format(count, last)
            count = 1
            last = c
            continue
        # else keep moving
        count += 1
        last = c
    # on exit, need to add last thing being counted
    string += "{}{}".format(count, last)
    return string


def count_and_say(n: int) -> str:
    if not 0 < n <= 30:
        raise ValueError("n must be a positive integer [1:30]")

    it = 1
    word = "1"

    while it < n:
        it += 1
        word = _say(word)

    return word
