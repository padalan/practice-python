"""
643. Maximum Average Subarray I
Easy
Topics
Companies

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000

 

Constraints:

    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104


"""
def largestAltitude(gain):
    current_altitude = 0
    max_altitude = 0
    
    # Iterate through the gain array
    for g in gain:
        current_altitude += g  # Update current altitude
        max_altitude = max(max_altitude, current_altitude)  # Track highest altitude
    
    return max_altitude

# Example usage:
print(largestAltitude([-5,1,5,0,-7]))  # Output: 1
print(largestAltitude([-4,-3,-2,-1,4,3,2]))  # Output: 0
