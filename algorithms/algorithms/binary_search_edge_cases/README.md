## Binary Search – Edge Case Exploration

### Problem
Binary search is an efficient algorithm for searching in sorted arrays, but it relies on strict assumptions.

### Key Assumption
The input array must be sorted.

### Edge Cases Tested
- Empty array
- Single-element array
- Duplicate values
- Unsorted input

### Observations
When the array is unsorted, binary search may return incorrect results without raising an error.

### Lesson Learned
Algorithm correctness depends on preconditions. An efficient algorithm is only correct when its assumptions are satisfied.
