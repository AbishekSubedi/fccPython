"""
bst_inorder_traversal.py

A module to implement a Binary Search Tree (BST) and perform in-order traversal.

Classes:
--------
TreeNode
    A class to represent a node in the BST.

BinarySearchTree
    A class to represent the BST and provide methods to manipulate it.

Example usage:
--------------
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
node = bst.search(10)
print(node)
"""


class TreeNode:
    """
    A class to represent a node in the Binary Search Tree.

    Attributes:
    -----------
    key : int
        The value of the node.
    left : TreeNode or None
        The left child of the node.
    right : TreeNode or None
        The right child of the node.
    """

    def __init__(self, key):
        """
        Initialize the TreeNode with a key.

        Parameters:
        -----------
        key : int
            The value of the node.
        """
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        """
        Return a string representation of the node.

        Returns:
        --------
        str
            The string representation of the node's key.
        """
        return str(self.key)


class BinarySearchTree:
    """
    A class to represent the Binary Search Tree and provide methods to manipulate it.

    Attributes:
    -----------
    root : TreeNode or None
        The root node of the BST.
    """

    def __init__(self):
        """
        Initialize the BinarySearchTree with an empty root.
        """
        self.root = None

    def _insert(self, node, key):
        """
        Recursively insert a key into the BST.

        Parameters:
        -----------
        node : TreeNode or None
            The current node in the BST.
        key : int
            The value to insert.

        Returns:
        --------
        TreeNode
            The node after insertion.
        """
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def insert(self, key):
        """
        Insert a key into the BST.

        Parameters:
        -----------
        key : int
            The value to insert.
        """
        self.root = self._insert(self.root, key)

    def _search(self, node, key):
        """
        Recursively search for a key in the BST.

        Parameters:
        -----------
        node : TreeNode or None
            The current node in the BST.
        key : int
            The value to search for.

        Returns:
        --------
        TreeNode or None
            The node with the specified key, or None if not found.
        """
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def search(self, key):
        """
        Search for a key in the BST.

        Parameters:
        -----------
        key : int
            The value to search for.

        Returns:
        --------
        TreeNode or None
            The node with the specified key, or None if not found.
        """
        return self._search(self.root, key)

    def _delete(self, node, key):
        """
        Recursively delete a key from the BST.

        Parameters:
        -----------
        node : TreeNode or None
            The current node in the BST.
        key : int
            The value to delete.

        Returns:
        --------
        TreeNode or None
            The node after deletion.
        """
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)

        return node

    def delete(self, key):
        """
        Delete a key from the BST.

        Parameters:
        -----------
        key : int
            The value to delete.
        """
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        """
        Find the node with the minimum value in the BST.

        Parameters:
        -----------
        node : TreeNode
            The current node in the BST.

        Returns:
        --------
        int
            The minimum value in the BST.
        """
        while node.left is not None:
            node = node.left
        return node.key

    def _inorder_traversal(self, node, result):
        """
        Recursively perform in-order traversal of the BST.

        Parameters:
        -----------
        node : TreeNode or None
            The current node in the BST.
        result : list of int
            The list to store the traversal result.
        """
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        """
        Perform in-order traversal of the BST.

        Returns:
        --------
        list of int
            The list of node values in in-order.
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result


# Example usage
bst = BinarySearchTree()
nodes = [50, 30, 16, 20, 40, 70, 60, 80]

for node1 in nodes:
    bst.insert(node1)

print('Search for 80:', bst.search(80))

print("Inorder traversal:", bst.inorder_traversal())

bst.delete(40)

print("Search for 40:", bst.search(40))

print('Inorder traversal after deleting 40:', bst.inorder_traversal())
