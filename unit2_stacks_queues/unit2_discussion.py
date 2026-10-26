
"""
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # The newest value is placed on top, so it is the first one removed (LIFO).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek reads the top value without changing the stack.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values join the back, while earlier arrivals remain at the front (FIFO).
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front reads the next value to be served without removing it.
        if self.is_empty():
            raise IndexError("Cannot view the front of an empty queue.")
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    history = Stack()

    for action in [
        "Open document",
        "Type a sentence",
        "Format heading",
        "Save file"
    ]:
        history.push(action)
        print(f"Added to undo history: {action}")

    print(f"Top action (next to undo): {history.peek()}")
    print("Undoing actions (most recent first):")

    while not history.is_empty():
        print(f"  Undid: {history.pop()}")

    # Test pop() and peek() on an empty stack.
    for label, operation in [
        ("pop()", history.pop),
        ("peek()", history.peek)
    ]:
        try:
            operation()
        except IndexError as error:
            print(f"Empty-stack {label} handled safely: {error}")

    # Test a stack containing only one item.
    one_item_stack = Stack()
    one_item_stack.push("Only item")

    print(f"Single-item stack pop: {one_item_stack.pop()}")
    print(
        "Single-item stack empty afterward: "
        f"{one_item_stack.is_empty()}"
    )

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    customers = Queue()

    for customer in ["Amina", "Ben", "Carlos", "Dara"]:
        customers.enqueue(customer)
        print(f"Customer joined the line: {customer}")

    print(f"Next customer to be served: {customers.front()}")
    print("Serving customers (first arrived, first served):")

    while not customers.is_empty():
        print(f"  Served: {customers.dequeue()}")

    # Test dequeue() and front() on an empty queue.
    for label, operation in [
        ("dequeue()", customers.dequeue),
        ("front()", customers.front)
    ]:
        try:
            operation()
        except IndexError as error:
            print(f"Empty-queue {label} handled safely: {error}")

    # Test a queue containing only one item.
    one_item_queue = Queue()
    one_item_queue.enqueue("Only customer")

    print(f"Single-item queue dequeue: {one_item_queue.dequeue()}")
    print(
        "Single-item queue empty afterward: "
        f"{one_item_queue.is_empty()}"
    )


if __name__ == "__main__":
    main()
