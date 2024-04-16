from __future__ import annotations

from typing import Callable, Optional


class Stack(list):
    def push(self, *args, **kwargs):
        # for python, append() is equivalent to push()
        self.append(*args, **kwargs)

    def has_items(self) -> int:
        return len(self) > 0


class Queue(list):
    def push(self, *args, **kwargs):
        # for python, insert(0, ...) is equivalent to push()
        self.insert(0, *args, **kwargs)

    def has_items(self) -> int:
        return len(self) > 0


class Node:
    def __init__(
        self, value: str, left: Optional[Node] = None, right: Optional[Node] = None
    ):
        self.value = str(value)
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def depth_visit_tree(root: Node, visit_fn: Optional[Callable] = print):
    stack = Stack()
    stack.push(root)

    def visit(node) -> None:
        # execute the visit_fn
        visit_fn(node)
        # and push n's children to the stack
        if node.right:
            stack.push(node.right)
        if node.left:
            stack.push(node.left)

    while stack.has_items():
        visit(stack.pop())


def breadth_visit_tree(root: Node, visit_fn: Optional[Callable] = print):
    queue = Queue()
    queue.push(root)

    def visit(node) -> None:
        # execute the visit_fn
        visit_fn(node)
        # and push n's children to the queue
        if node.left:
            queue.push(node.left)
        if node.right:
            queue.push(node.right)

    while queue.has_items():
        visit(queue.pop())
