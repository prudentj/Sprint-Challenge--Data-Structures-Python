"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = 0

    # Insert the given value into the tree
    def insert(self, value):
        # If it is greater than or equal to add it to the right
        # If there is a node there pass the value it it
        # Else make a node
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
                self.right.level = self.level + 1
        # Less than add it to the left
        # If there is a node there pass the value it it
        # Else make a node
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
                self.left.level = self.level + 1

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # This is the value we seek
        if self.value == target:
            return True
        # If the value we want is here it is to the right
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                # It does not exist
                return False
        # If the value we want is here it is to the left
        else:
            if self.right:
                return self.right.contains(target)
            else:
                # It does not exist
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    # If left or right exist call that function
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # When there isn't a node
        if node == None:
            return
        queue = []
        # Appends itself
        queue.append(node)
        while(len(queue) > 0):
            print(queue[0].value)
            current = queue.pop(0)
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        print(node.value)

        if node.right:
            node.right.dft_print(node.right)
        if node.left:
            node.left.dft_print(node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# # bst.in_order_print(bst)
# bst.dft_print(bst)
# # "1\n8\n5\n7\n6\n3\n4\n2\n" or
# # output == "1\n8\n5\n3\n2\n4\n7\n6\n")
