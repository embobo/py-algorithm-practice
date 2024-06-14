"""
You are given an integer array height of length n. There are n vertical lines drawn such that the
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the
most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example:

|
|
|    0              0
|    0--------------0-----0
|    0  0           0     0
|    0  0     0     0     0
|    0  0     0  0  0     0
|    0  0     0  0  0  0  0
|    0  0  0  0  0  0  0  0
|_0__0__0__0__0__0__0__0__0____
  0  1  2  3  4  5  6  7  8

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
"""

from typing import List


def max_area(arr: List[int]) -> int:
    max = 0
    for w in range(1, len(arr)):
        # pass through the array checking largest volume per width (w) size
        for i in range(0, len(arr) - w):
            min_h = min([arr[i], arr[i + w]])
            area = w * min_h
            if area > max:
                max = area

    return max
