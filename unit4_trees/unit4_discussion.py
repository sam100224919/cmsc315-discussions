"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        # Each new node started with two empty child references.
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        # The root stayed None until the first value was inserted.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The helper returned the root reference, including when the
        # first insertion created a node in an empty tree.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # An empty position marked where the new value belonged.
        if node is None:
            return Node(value)

        # Smaller values went left and larger values went right.
        # This ordering narrowed the next search path at each comparison.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Duplicate values were ignored so each employee ID appeared once.

        # Returning the node kept the updated subtree connected to its parent.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # A BST search followed only one branch at each comparison.
        # A balanced tree therefore examined about log2(n) levels rather
        # than checking every item as a linear search might do.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Reaching an empty child meant the value was not in the tree.
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # The helper filled a list in ascending order.
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # An empty subtree had no value to append.
        if node is None:
            return

        # Left-node-right order produced ascending values because smaller
        # values were stored left and larger values were stored right.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    # Employee IDs were inserted in a middle-first order to create a
    # balanced example. Each comparison selected only one subtree, reducing
    # the remaining search space at every level.
    employee_ids = [1050, 1025, 1075, 1010, 1035, 1060, 1090]
    employee_tree = BST()
    for employee_id in employee_ids:
        employee_tree.insert(employee_id)
    print("Employee IDs inserted:", employee_ids)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    # In-order traversal visited left, node, then right. Because smaller
    # values were stored left and larger values right, output was sorted.
    print("Sorted employee IDs:", employee_tree.inorder())

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # Existing IDs returned True; missing IDs returned False.
    # Each search compared an ID and continued down only one subtree.
    for employee_id in [1010, 1075, 1005, 1100]:
        print(f"Search for {employee_id}: {employee_tree.search(employee_id)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    # An empty tree had no root, so traversal returned [] and search
    # returned False without attempting to access a node.
    empty_tree = BST()
    print("Empty-tree traversal:", empty_tree.inorder())
    print("Search empty tree for 1050:", empty_tree.search(1050))

    # Duplicate insertion was ignored; traversal showed each ID only once.
    employee_tree.insert(1050)
    print("After inserting duplicate 1050:", employee_tree.inorder())



if __name__ == "__main__":
    main()