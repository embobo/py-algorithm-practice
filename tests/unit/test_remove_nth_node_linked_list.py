from typing import List

import pytest

from src.algorithms.remove_nth_node_linked_list import (
    ListNode,
    remove_nth_from_end,
    to_linked_list,
)


class TestRemoveNthNodeLinkedList:
    @pytest.mark.parametrize(
        "input, to_remove, expected",
        [
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 2, [1, 8, 6, 2, 5, 4, 8, 7]),
            ([8, 0, 0, 0, 9], 5, [0, 0, 0, 9]),
            ([0, 1, 15, 10, 1], 1, [0, 1, 15, 10]),
            ([1], 1, []),
        ],
    )
    def test_remove_nth_node_linked_list(
        self, input: List, to_remove: int, expected: List
    ):
        print("input: {}".format(input))
        head = to_linked_list(input)
        print("linked list head: {}".format(head.val))
        result = remove_nth_from_end(head, to_remove)
        out = result.to_list() if isinstance(result, ListNode) else []
        assert out == expected
