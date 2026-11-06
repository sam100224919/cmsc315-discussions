# Unit 4 Discussion: Binary Search Trees

## Overview

I implemented a Binary Search Tree (BST) in Python to organize employee records by employee ID. The program demonstrated recursive insertion, recursive searching, in-order traversal, and edge-case handling.

## Implementation

- I created a `Node` class that stored a value and references to left and right children.
- I created a `BST` class with a root reference.
- I implemented insertion recursively. Values smaller than the current node were placed in the left subtree, and larger values were placed in the right subtree.
- I ignored duplicate values so an employee ID appeared only once.
- I implemented recursive searching. The search returned `True` when it found a value and `False` when it reached an empty position.
- I implemented in-order traversal by visiting the left subtree, current node, and right subtree. This returned the values in ascending order.

## Demonstration and Testing

I inserted seven employee IDs in a middle-first order: `1050, 1025, 1075, 1010, 1035, 1060, 1090`. This produced a balanced example with values in both the left and right subtrees. I displayed the inserted values and the sorted in-order traversal.

I tested searches for two IDs that were present (`1010` and `1075`) and two that were absent (`1005` and `1100`). I also tested an empty tree by traversing it and searching it, and tested duplicate insertion by inserting `1050` a second time.

## Real-World Application

I used employee IDs as the example data. A company could use a BST to organize employee records by ID and locate a record through comparisons rather than scanning every record. The tree's performance depended on its shape and insertion order.

## Performance Reflection

A balanced BST can locate a value in approximately `O(log n)` time because each comparison eliminates one subtree from consideration. In-order traversal takes `O(n)` time because it visits every node. However, a BST can become skewed when values are inserted in sorted or nearly sorted order. In that case, searching and insertion can degrade to `O(n)`, similar to a linked list. A self-balancing tree, such as an AVL tree or Red-Black tree, can help maintain efficient height.

## Discussion Board Reflection

While completing this assignment, I learned how a Binary Search Tree organized values through recursive insertion and searching. I also practiced in-order traversal and saw how visiting the left subtree, current node, and right subtree produced sorted output. One challenge was understanding how each recursive call returned an updated node reference. I addressed this by returning the new or existing node at each step so that changes remained connected to the root. I used employee IDs as a real-world example and inserted the middle value first to create a more balanced tree. A balanced BST could reduce search work to approximately `O(log n)` because each comparison eliminated one subtree. This was more efficient than a linear search, which could require checking every value. However, I learned that insertion order mattered. If values were inserted sequentially, the tree could become skewed and behave like a linked list, causing search performance to fall to `O(n)`. I also tested empty-tree searches and duplicate insertion.
