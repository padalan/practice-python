"""
283. Move Zeroes
Solved
Easy
Topics
Companies
Hint

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

 

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1

 
Follow up: Could you minimize the total number of operations done?
"""
def moveZeroes(nums):
    # Pointer to keep track of where the next non-zero element should go
    last_non_zero_found_at = 0
    
    # Move all non-zero numbers to the front of the array
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_found_at] = nums[i]
            last_non_zero_found_at += 1
    
    # Fill the remaining positions with zeroes
    for i in range(last_non_zero_found_at, len(nums)):
        nums[i] = 0

# Example usage:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

nums = [0]
moveZeroes(nums)
print(nums)  # Output: [0]
