"""
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.

"""
def gcd(a, b):
    # We loop until b becomes zero.
    while b != 0:
        # Step 1: Update a and b values.
        # Calculate a % b (remainder of a divided by b)
        remainder = a % b
        # Update a to the value of b (swap values)
        a = b
        # Update b to the remainder
        b = remainder
    # When b becomes zero, a holds the GCD value, so we return it.
    return a
"""
import math
print(math.gcd(48, 18))  # Output: 6
"""

def gcdOfStrings(str1, str2):
    # Check if concatenation str1+str2 equals str2+str1, otherwise return ""
    if str1 + str2 != str2 + str1:
        return ""
    
    # Manually calculate the GCD of the lengths of the two strings
    gcd_length = gcd(len(str1), len(str2))
    
    # Return the substring of str1 up to the gcd_length
    return str1[:gcd_length]

# Example usage
print(gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(gcdOfStrings("LEET", "CODE"))    # Output: ""