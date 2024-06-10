"""
LeetCode prompt
ref: https://leetcode.com/problems/valid-parenthesis-string/description/

Given a string s containing only three types of characters: '(', ')' and '*',
return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left
parenthesis '(' or an empty string "".
"""


def parentheses_valid(string: str) -> bool:
    count = 0
    wildcards = 0

    for c in string:
        if c == "(":
            count += 1
        elif c == ")":
            if count > 0:
                count -= 1
            elif wildcards > 0:
                wildcards -= 1
            else:
                # hit a close with no open
                return False
        elif c == "*":
            wildcards += 1

    # if count is 0, all opens were explicitly closed
    # if count is nonzero, but there are available wildcards, opens can be closed with wilds
    return count == 0 or (wildcards >= count)
