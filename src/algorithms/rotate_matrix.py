"""
Leetcode prompt
ref: https://leetcode.com/problems/rotate-image/description/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Assume:
  * n == matrix.length == matrix[i].length
  * 1 <= n <= 20
  * -1000 <= matrix[i][j] <= 1000

ex:

1 2 3      7 4 1
4 5 6  ->  8 5 2
7 8 9      9 6 3

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]


ex 2:

5  1  9  11     15 13 2  5
2  4  8  10     14 3  4  1
13 3  6  7      12 6  8  9
15 14 12 16     16 7  10 11

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

from typing import List


def print_matrix(matrix):
    for row in range(0, len(matrix)):
        print(matrix[row])


def rotate_matrix(matrix: List[List[int]]):
    """
    Rotate 90 degrees clockwise in place
    tl  --->  tr
    ^         |
    |         v
    bl  <---  br
    """
    print("INPUT MATRIX")
    print_matrix(matrix)
    n = len(matrix)
    # iterate through each of the TL position indices
    for row in range(0, int(n / 2)):
        for col in range(row, n - 1 - row):
            print(f"TL at {row}, {col}")
            tl = matrix[row][col]
            tr = matrix[row][n - 1 - col]
            br = matrix[n - 1 - row][n - 1 - col]
            bl = matrix[n - 1 - row][col]
            print("TL {}, TR {}, BL {}, BR {}".format(tl, tr, bl, br))
            matrix[row][col] = bl
            matrix[row][n - 1 - col] = tl
            matrix[n - 1 - row][n - 1 - col] = tr
            matrix[n - 1 - row][col] = br
            print("current matrix")
            print_matrix(matrix)
