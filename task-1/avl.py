class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        right_child.height = 1 + max(self.height(right_child.left), self.height(right_child.right))
        return right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        left_child.height = 1 + max(self.height(left_child.left), self.height(left_child.right))
        return left_child

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return AVLNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance_factor(root)
        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
        return root

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, root):
        if root:
            self._inorder_traversal(root.left)
            print(root.key)
            self._inorder_traversal(root.right)

    def words_with_prefix(self, prefix):
        words = []
        self._words_with_prefix(self.root, prefix, words)
        return words

    def _words_with_prefix(self, node, prefix, words):
        if node is None:
            return
        if node.key.startswith(prefix):
            self._words_with_prefix(node.left, prefix, words)
            words.append(node.key)
            self._words_with_prefix(node.right, prefix, words)
        elif prefix < node.key:
            self._words_with_prefix(node.left, prefix, words)
        else:
            self._words_with_prefix(node.right, prefix, words)