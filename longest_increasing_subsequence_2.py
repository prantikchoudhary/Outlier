#This program is returns the longest increasing subsequence instead of longest increasing contiguous subsequence which does not adhere to the specific requirements given in the prompt instructions.
#Though the program compiles free of any runtime errors but would not be accepted.

from bisect import bisect_left

def longest_increasing_subsequence_2(nums):
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
nums = [1, 2, 3, 4, 7, 101, 6]
result = longest_increasing_subsequence_2(nums)
print("Longest Increasing Subsequence:", result)