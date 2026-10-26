# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explored two fundamental data structures: stacks and queues. I implemented a stack using a Python list and a queue using `collections.deque`.

## Stack Implementation

I implemented the `Stack` class with `push()`, `pop()`, `peek()`, and `is_empty()` methods. The `push()` method added values to the top of the stack, while `pop()` removed and returned the most recently added value. The `peek()` method returned the top value without removing it.

I demonstrated last-in-first-out (LIFO) behavior using a text-editor undo history. The most recent action, “Save file,” was undone first, followed by earlier actions. I also tested empty-stack operations and a stack containing only one item.

## Queue Implementation

I implemented the `Queue` class using `collections.deque`. The `enqueue()` method added values to the back of the queue, while `dequeue()` removed and returned the value at the front. The `front()` method returned the next value without removing it.

I demonstrated first-in-first-out (FIFO) behavior using a customer line. Amina, Ben, Carlos, and Dara were served in the order they arrived. I also tested empty-queue operations and a queue containing only one item.

## Edge Cases and Testing

I tested `pop()` and `peek()` on an empty stack and `dequeue()` and `front()` on an empty queue. Each operation raised a descriptive `IndexError`, which the demonstration handled. I also confirmed that removing the only item from a stack or queue left that structure empty.

## Memory Usage and Performance

Both structures stored one reference for each item added, so their memory use grew linearly with the number of stored items, or O(n). Stack insertion and removal at the end of a Python list are amortized O(1). Queue insertion at the back and removal from the front using `collections.deque` are O(1) operations.

## Learning Reflection

Through this assignment, I practiced implementing stack and queue operations and connecting them to real-world applications. I learned that LIFO is appropriate for undo histories because the most recent action should be reversed first, while FIFO is appropriate for service lines because the earliest arrival should be handled first. Testing empty structures helped me understand the importance of error handling. Testing single-item structures also helped verify that the data structures behaved correctly at boundary conditions.