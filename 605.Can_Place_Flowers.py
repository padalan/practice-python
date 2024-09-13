"""
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

 

Constraints:

    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length

"""
class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        count = 0  # To track the number of flowers we can plant
        for i in range(len(flowerbed)):  # Loop through each plot in the flowerbed
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if the left plot is empty or we're at the start
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                # Check if the right plot is empty or we're at the end
                empty_right_plot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both the left and right plots are empty, plant a flower
                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1  # Plant the flower
                    count += 1  # Increase the flower count
                    
        # Check if we planted enough flowers
        return count >= n

# Test cases
flowerbed1 = [1, 0, 0, 0, 1]
n1 = 1
print(Solution().canPlaceFlowers(flowerbed1, n1))  # Output: True

flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
print(Solution().canPlaceFlowers(flowerbed2, n2))  # Output: False

flowerbed3 = [0, 0, 1, 0, 0]
n3 = 1
print(Solution().canPlaceFlowers(flowerbed3, n3))  # Output: True

flowerbed4 = [0, 0, 0, 0, 0]
n4 = 2
print(Solution().canPlaceFlowers(flowerbed4, n4))  # Output: True

flowerbed5 = [1, 0, 1, 0, 1]
n5 = 1
print(Solution().canPlaceFlowers(flowerbed5, n5))  # Output: False
