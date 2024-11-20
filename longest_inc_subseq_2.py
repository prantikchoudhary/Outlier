from bisect import bisect_left

def longest_increasing_subsequence(nums):
    """
    Finds the longest contiguous increasing subsequence in O(n log n) time complexity.
    
    Parameters:
    nums (list[int]): The unsorted array of integers.
    
    Returns:
    list[int]: The longest contiguous increasing subsequence.
    """
    if not nums:
        return []

    # Auxiliary array to store the end elements of increasing subsequences
    subsequence_ends = []
    positions = []  # Store indices to reconstruct the subsequence

    for i, num in enumerate(nums):
        pos = bisect_left(subsequence_ends, num)  # Find position to replace or append
        if pos == len(subsequence_ends):
            subsequence_ends.append(num)
            positions.append((pos, i))  # Append index and position
        else:
            subsequence_ends[pos] = num
            positions.append((pos, i))  # Update index and position

    # Reconstruct the subsequence using positions
    longest_seq = []
    pos, idx = len(subsequence_ends) - 1, -1
    for p, i in reversed(positions):
        if p == pos and (idx == -1 or i < idx):
            longest_seq.append(nums[i])
            pos -= 1
            idx = i
    return longest_seq[::-1]  # Reverse to get the sequence in order

# Example usage:
nums = [1, 3, 5, 4, 7, 8, 6]
result = longest_increasing_subsequence(nums)
print("Longest Increasing Subsequence:", result)