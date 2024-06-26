# ref: https://www.hackerrank.com/challenges/tree-huffman-decoding/problem
class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None


# Enter your code here. Read input from STDIN. Print output to STDOUT
def decode_huff(root: Node, encoded_s: str) -> str:
    node: Node = root
    word: str = ""
    for c in encoded_s:
        if c == "1":
            node = node.right
        if c == "0":
            node = node.left
        if not node.right and not node.left:
            # leaf
            word += node.data
            node = root  # reset node to root for next sequence
    return word
