class AVLTreeNode:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return AVLTreeNode(value)
        elif value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1:
            if value < node.left.value:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
        if balance < -1:
            if value > node.right.value:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node):
        result = []
        if node:
            result += self._inorder_traversal_recursive(node.left)
            result.append(node.value)
            result += self._inorder_traversal_recursive(node.right)
        return result

# Test the AVL Tree
avl = AVLTree()
avl.insert(5)
avl.insert(3)
avl.insert(7)
avl.insert(2)
avl.insert(4)
avl.insert(6)
avl.insert(8)
print("AVL Tree Inorder Traversal:", avl.inorder_traversal())  # Should print [2, 3, 4, 5, 6, 7, 8]
