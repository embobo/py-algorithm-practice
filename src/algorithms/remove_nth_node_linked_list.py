"""
ref: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Remove Nth Node From End of List
Medium
Topics
Companies
Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
  Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
  Input: head = [1], n = 1
  Output: []

Example 3:
  Input: head = [1,2], n = 1
  Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return "{}".format(self.to_list())

    def to_list(self) -> List:
        # treats 'self' as the head
        vals = []
        node = self
        while node is not None:
            vals.append(node.val)
            node = node.next
        return vals


def to_linked_list(l: List) -> ListNode:  # noqa E741
    # assumes len(l) > 0
    head = ListNode(l[0])
    current = head
    for val in l[1:]:
        node = ListNode(val)
        current.next = node
        current = node
    return head


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    (1 -> 8 -> 6 -> 2 -> 5 -> 0 -> 8 -> 3 -> 7), 4
                              ^remove
    1
    ^leading  -- count = 4
    1 -> 8
         ^leading  -- count = 3
    1 -> 8 -> 6
              ^leading  -- count = 2
    1 -> 8 -> 6 -> 2
                   ^leading  -- count = 1
    1 -> 8 -> 6 -> 2 -> 5
    ^ lagging           ^ leading  -- count = 0
    1 -> 8 -> 6 -> 2 -> 5 -> 0
         ^ lagging           ^ leading
    1 -> 8 -> 6 -> 2 -> 5 -> 0 -> 8
              ^ lagging           ^ leading
    1 -> 8 -> 6 -> 2 -> 5 -> 0 -> 8 -> 3
                   ^ lagging           ^ leading
    1 -> 8 -> 6 -> 2 -> 5 -> 0 -> 8 -> 3 -> 7  !! -> None
                        ^ lagging           ^ leading

    # item to remove is now lagging.next
    """
    leading: ListNode = head
    lagging: ListNode = None
    count: int = n

    while leading.next:
        count -= 1
        leading = leading.next
        if count == 0:
            lagging = head
        if count < 0:
            lagging = lagging.next

    # Three exit conditions:
    #  1. lagging is set, indicating lagging.next is the node to remove
    #  2. count = 1, indicating the head node is the node to remove
    #  3. count > 1, indicating n is greater than the number of nodes in the list (return None)

    if count > 1:
        return None
    if count == 1:
        return head.next
    if lagging:
        lagging.next = lagging.next.next
        return head

    print("AH! ERR")
