""" 724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0 

Constraints:

    1 <= nums.length <= 104
    -1000 <= nums[i] <= 1000

"""
def pivotIndex(nums):
    # Initialize left_sum to 0, representing the sum of elements to the left of the current index
    left_sum = 0
    
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # Iterate through the array with both index and element
    for i, num in enumerate(nums):
        # Check if the sum of elements to the left is equal to the sum of elements to the right
        # Right sum is total_sum - left_sum - current element (num)
        if left_sum == total_sum - left_sum - num:
            return i  # Return the index if the condition is satisfied
        left_sum += num  # Update left_sum for the next iteration
    
    return -1  # Return -1 if no pivot index is found

# Test cases
print(pivotIndex([1, 7, 3, 6, 5, 6]))  # Output: 3
print(pivotIndex([1, 2, 3]))           # Output: -1
print(pivotIndex([2, 1, -1]))          # Output: 0
print(pivotIndex([0, 0, 0, 0]))        # Output: 0
print(pivotIndex([1, -1, 2, -1, 1]))   # Output: 2
