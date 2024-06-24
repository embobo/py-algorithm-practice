#!/bin/python3

import os
import sys
import traceback as tb
from typing import List

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


# ===== Brute Force ===== #
# does not work for large quantities of queries
def compute(n: int, queries: List[List[int]]) -> int:
    arr = [0] * n
    for q in queries:
        s = q[0] - 1
        e = q[1]
        k = q[2]
        arr[s:e] = [v + k for v in arr[s:e]]
    return max(arr)


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def _update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx

    def range_update(self, l, r, delta):  # noqa E741
        self._update(l, delta)
        if r + 1 <= self.n:
            self._update(r + 1, -delta)

    def query(self, idx):
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= idx & -idx
        return sum


def tree_compute(n: int, queries: List[List[int]]) -> int:
    arr = FenwickTree(n)

    for q in queries:
        s = q[0]
        e = q[1]
        k = q[2]
        arr.range_update(s, e, k)
    # print(arr.tree)

    max_value = 0
    for i in range(1, n + 1):
        max_value = max(max_value, arr.query(i))

    return max_value


def array_manipulation(input: str) -> int:
    """
    parse string input into values to process in _manipulate
    """
    data = input.rstrip().split("\n")

    n, m = tuple(map(int, data[0].split()))

    queries = [list(map(int, q.rstrip().split())) for q in data[1:]]

    if len(queries) != m:
        raise ValueError(
            f"Did not receive expected number of queries: got {len(queries)} but expected {m}"
        )

    result = tree_compute(n, queries)

    print(result)
    return result


if __name__ == "__main__":
    try:
        fptr = open(os.environ["OUTPUT_PATH"], "w")

        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        queries = []

        for _ in range(m):
            queries.append(list(map(int, input().rstrip().split())))

        result = tree_compute(n, queries)

        fptr.write(str(result) + "\n")

        fptr.close()
    except Exception as e:
        print(f"{e} - {tb.format_exc()}", file=sys.stderr)
        print(f"{e} - {tb.format_exc()}", file=sys.stdout)
        raise e
