# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compared Bubble Sort and Merge Sort by implementing both algorithms in Python, testing them with multiple datasets, demonstrating edge cases, and considering their efficiency.

## Learning Objectives

- Implemented Bubble Sort.
- Implemented Merge Sort.
- Applied recursion and the divide-and-conquer strategy.
- Compared algorithm efficiency and behavior.

## Implementation

### Bubble Sort

Bubble Sort was implemented with adjacent comparisons and swaps. The function first copied the input list, so the caller's original list was not changed. It also used an early-exit condition: if a complete pass made no swaps, the list was already sorted and the algorithm stopped.

- Worst-case time complexity: O(n²).
- Average-case time complexity: O(n²).
- Best-case time complexity with the early-exit check: O(n).
- Auxiliary space: O(n) for the copied list; the sorting process itself uses O(1) additional space.
- Stability: Stable, because equal values are not swapped.

### Merge Sort

Merge Sort was implemented recursively. The list was divided into two halves until each sublist contained zero or one item. The sorted halves were then combined by the `merge()` function.

- Best-, average-, and worst-case time complexity: O(n log n).
- Auxiliary space: O(n) for the merged output and temporary lists.
- Stability: Stable, because `merge()` selects from the left half when values are equal.

## Datasets and Edge Cases

The program tested two datasets:

1. An unsorted dataset containing eight values.
2. A second dataset containing different values and a partially ordered pattern.

Both algorithms produced matching sorted results for each dataset.

The program also tested:
- An empty list, which remained empty.
- An already sorted list, which remained in ascending order.
- A reverse-sorted list, which was reordered into ascending order.
- A list containing duplicates, which retained all duplicate values.
- A single-element list, which remained unchanged.

Both sorting functions returned new lists and preserved the original input.

## Performance Analysis

Bubble Sort is straightforward and can be effective for very small lists or data that is already sorted, especially when an early-exit check is used. However, its average and worst-case running times grow quadratically. As the input becomes much larger, the number of comparisons and swaps can become expensive.

Merge Sort scales better for large datasets because it divides the input into smaller parts and performs O(n log n) work overall. Its running time is more consistent across different input orders. The trade-off is that Merge Sort requires additional memory for the temporary lists created during splitting and merging.

For a streaming platform, Merge Sort would be a stronger choice for sorting large content lists by rating or popularity. Its stability can preserve the prior relative order of items with equal ratings, provided the original order represents a meaningful tie-breaker. For a very small personal playlist, Bubble Sort could be acceptable because its implementation is simple and the input is small. Merge Sort also offers more potential for parallelization: its left and right halves can be sorted independently before they are merged. On distributed servers, that work could be assigned to separate workers, but network communication, data movement, synchronization, and the final merge add overhead. Bubble Sort is less suitable for parallel execution because its adjacent comparisons and swaps occur in dependent passes. In a production system, the platform would need to measure whether the dataset is large enough for the benefits of parallel Merge Sort to outweigh that overhead.

## Real-World Sorting Example

A streaming service could sort a user's recommended movies by rating. Merge Sort is appropriate for a large recommendation list because its O(n log n) time complexity is more scalable than Bubble Sort's O(n²) average and worst-case complexity. A stable merge operation can also retain the existing order of movies that have the same rating.

## Discussion Board Reflection (150–200 words)

While completing this assignment, I learned how two sorting algorithms can produce the same ordered result while using different strategies and resources. I implemented Bubble Sort by comparing adjacent values and swapping them when they were out of order. I implemented Merge Sort using recursion, dividing the list into smaller halves, and merging the sorted halves. I also learned why stability matters when records have equal ratings and why preserving the original input can make a function safer to use.

One challenge was understanding how the recursive calls in Merge Sort eventually return to the merge step. I addressed this by separating the merging logic into its own function and testing empty, single-item, duplicate, sorted, and reverse-sorted lists. Bubble Sort was easier to follow and can stop early when a list is already sorted, but its average and worst-case time complexity is O(n²). Merge Sort consistently runs in O(n log n), making it more suitable for large datasets, although it uses additional memory. I would use Bubble Sort for tiny lists and Merge Sort for large recommendation lists.

## Submission Checklist

- [x] Implemented Bubble Sort.
- [x] Implemented Merge Sort.
- [x] Implemented the merge helper function.
- [x] Tested two datasets.
- [x] Demonstrated more than two edge cases.
- [x] Compared the algorithms' performance characteristics.
- [x] Included a real-world sorting example.
- [x] Added the 150–200 word reflection.
- [ ] Committed and pushed the completed Python file and README to GitHub.
- [ ] Added the GitHub repository link to the initial discussion post.
- [ ] Submitted at least two peer responses.

**Note:** The assignment folder's separate `submission_checklist.md` was not uploaded, so the checklist above was based on the README requirements and the provided starter-code prompts.
