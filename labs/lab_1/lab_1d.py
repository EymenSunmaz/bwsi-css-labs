"""
lab_1d.py

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Derived from LeetCode problem: https://leetcode.com/problems/two-sum/ (leetcode easy)
"""

# TODO: Find and resolve the bug in the following implementation. Create unit tests to verify your fix.
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Function that takes in a list of integers and a target integer, and returns the indices of the two numbers that add up to the target.

    Args:
        nums (list[int]): List of integers.
        target (int): Target integer.
    
    Returns:
        list[int]: Indices of the two numbers that add up to the target.
    """
    for i in range(0,len(nums)-1):
        for x in range(i,len(nums)-1):
            complement = nums[x] + nums[x+1]
            if complement == target:
                return [x,x+1]

    return []  # In case there is no solution, though the problem guarantees one exists.

# Example usage:
def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")

if __name__ == "__main__":
    main()