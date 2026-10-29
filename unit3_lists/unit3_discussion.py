"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # list.insert() places the value at index and shifts later elements right.
    # Inserting near the beginning is O(n) because many elements may shift;
    # inserting at the end is amortized O(1) for Python's dynamic array.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Validate explicitly so invalid indexes do not accidentally delete an item
    # from the end of the list (Python normally accepts negative indexes).
    if not isinstance(index, int) or isinstance(index, bool):
        return None
    if index < 0 or index >= len(lst):
        # Returning None makes an invalid deletion safe for this assignment.
        return None

    # Removing an element shifts later elements left to fill the gap.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Linear search checks elements one at a time from left to right.
    # In the worst case, every element must be checked, so its time complexity is O(n).
    for index, item in enumerate(lst):
        if item == value:
            return index
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    values = ["Ava", "Ben", "Carlos", "Dina"]
    print(f"Original list: {values}")

    # Insert at index 0; existing elements shift one position to the right.
    insert_at(values, 0, "Zoe")
    print(f"After inserting 'Zoe' at the beginning: {values}")

    # Insert near the middle; the items after that index shift right.
    insert_at(values, 3, "Mia")
    print(f"After inserting 'Mia' in the middle: {values}")

    # Insert at len(list), which adds the new item to the end.
    insert_at(values, len(values), "Eli")
    print(f"After inserting 'Eli' at the end: {values}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    removed = delete_at(values, 0)
    print(f"Removed from the beginning: {removed}; updated list: {values}")

    middle_index = len(values) // 2
    removed = delete_at(values, middle_index)
    print(f"Removed from the middle (index {middle_index}): {removed}; updated list: {values}")

    removed = delete_at(values, len(values) - 1)
    print(f"Removed from the end: {removed}; updated list: {values}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    existing_value = values[1]
    print(f"Searching for existing value '{existing_value}': index {search_value(values, existing_value)}")
    missing_value = "Nora"
    print(f"Searching for missing value '{missing_value}': index {search_value(values, missing_value)} (-1 means not found)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    # Invalid deletion returns None and leaves the list unchanged.
    edge_values = ["Only item"]
    print(f"Before invalid deletion: {edge_values}")
    invalid_result = delete_at(edge_values, 5)
    print(f"Deleting at invalid index 5 returned {invalid_result}; list remains {edge_values}")

    # Inserting into an empty list is valid; deleting its only item empties it.
    empty_values = []
    insert_at(empty_values, 0, "First")
    print(f"After inserting into an empty list: {empty_values}")
    print(f"Deleting its only item returned: {delete_at(empty_values, 0)}")
    print(f"List after deleting its only item: {empty_values}")

    # Searching an empty list returns -1 because there are no elements to inspect.
    print(f"Searching an empty list returns: {search_value([], 'anything')}")


if __name__ == "__main__":
    main()
