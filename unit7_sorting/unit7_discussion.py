"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.
    """
    result = lst.copy()  # Work on a copy so the original list is preserved.
    n = len(result)

    # Each pass moves the largest unsorted value to its final position.
    for end in range(n - 1, 0, -1):
        swapped = False

        # Compare adjacent values within the unsorted portion.
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = (
                    result[index + 1],
                    result[index],
                )
                swapped = True

        # Stop early if a full pass did not require any swaps.
        if not swapped:
            break

    return result


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.
    """
    # Empty and one-element lists are already sorted (base case).
    if len(lst) <= 1:
        return lst.copy()

    # Divide the list into two smaller halves.
    midpoint = len(lst) // 2
    left_half = merge_sort(lst[:midpoint])
    right_half = merge_sort(lst[midpoint:])

    # Combine the recursively sorted halves.
    return merge(left_half, right_half)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    left_index = 0
    right_index = 0

    # Repeatedly append the smaller next value from either sorted half.
    # Choosing the left value on a tie preserves stability.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any values that remain in either half.
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def display_comparison(dataset_name, values):
    """Display both sorting results and verify that the input was unchanged."""
    original = values.copy()
    print(f"\n=== {dataset_name} ===")
    print("Original:", values)

    bubble_result = bubble_sort(values)
    merge_result = merge_sort(values)

    print("Bubble Sort:", bubble_result)
    print("Merge Sort: ", merge_result)
    print("Results match:", bubble_result == merge_result)
    print("Original unchanged:", values == original)


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.
    dataset_one = [42, 7, 19, 3, 28, 11, 35, 2]
    display_comparison("DATASET #1", dataset_one)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.
    dataset_two = [5, 8, 12, 4, 9, 15, 14, 20, 18]
    display_comparison("DATASET #2", dataset_two)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.
    edge_cases = [
        ("Empty list", []),
        ("Already sorted list", [1, 2, 3, 4, 5]),
        ("Reverse-sorted list", [5, 4, 3, 2, 1]),
        ("Duplicate values", [4, 2, 4, 1, 2, 1]),
        ("Single-element list", [9]),
    ]

    print("\n=== EDGE CASE TESTS ===")
    for description, values in edge_cases:
        bubble_result = bubble_sort(values)
        merge_result = merge_sort(values)
        print(f"{description}: {values}")
        print(f"  Bubble Sort: {bubble_result}")
        print(f"  Merge Sort:  {merge_result}")
        print(f"  Results match: {bubble_result == merge_result}")

    # Confirm that the sorting functions did not mutate their input.
    original = [3, 1, 2]
    bubble_sort(original)
    merge_sort(original)
    print("\nInput-preservation check:", original == [3, 1, 2])


if __name__ == "__main__":
    main()
