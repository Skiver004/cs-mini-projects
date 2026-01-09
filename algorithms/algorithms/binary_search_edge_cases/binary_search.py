def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Edge case tests
if __name__ == "__main__":
    print(binary_search([], 5))                  # empty list
    print(binary_search([10], 10))                # single element
    print(binary_search([1, 2, 2, 2, 3], 2))       # duplicates
    print(binary_search([3, 1, 2], 2))             # unsorted list
