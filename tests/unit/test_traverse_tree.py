from src.algorithms.traverse_tree import Node, breadth_visit_tree, depth_visit_tree


class TestDepthVisitTree:
    def make_tree(self) -> Node:
        """
             a
          b     c
        d   e     f
              g

        depth first: a, b, d, e, g, c, f
        breadth first: a, b, c, d, e, f, g
        """
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.right = g
        return a

    def test_depth_traverse(self):
        root = self.make_tree()
        output = list()

        def visit_fn(node):
            output.append(node.value)

        depth_visit_tree(root, visit_fn=visit_fn)
        assert output == ["a", "b", "d", "e", "g", "c", "f"]

    def test_breadth_traverse(self):
        root = self.make_tree()
        output = list()

        def visit_fn(node):
            output.append(node.value)

        breadth_visit_tree(root, visit_fn=visit_fn)
        print(output)
        assert output == ["a", "b", "c", "d", "e", "f", "g"]
