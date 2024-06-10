"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-2^31 <= x <= 2^31 - 1
-2147483648 <= x <= 2147483647
"""


def reverse_integer(x: int) -> int:
    if not -2147483648 <= x <= 2147483647:
        return 0
    n_str = str(x) if x >= 0 else str(x)[1:]
    num = int(n_str[::-1])
    num = num * -1 if x < 0 else num
    return num
