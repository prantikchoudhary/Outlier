# Write a Python function that takes an unsorted array of integers and returns the longest contiguous increasing subsequence. The function should run in O(n log n) time complexity.

def longest_contiguous_increasing_subsequence(arr):
    """
    Finds the longest contiguous increasing subsequence of an array in O(n) time.

    Args:
        arr: The input array of integers.

    Returns:
        A list representing the longest contiguous increasing subsequence.
    """
    if not arr:
        return []

    max_length = 1
    current_length = 1
    end_index = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_length += 1
        else:
            current_length = 1  # Reset the length for a new subsequence

        if current_length > max_length:
            max_length = current_length
            end_index = i

    # Reconstruct the subsequence
    start_index = end_index - max_length + 1
    return arr[start_index:end_index + 1]