"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.

"""


def reverseVowels(s: str) -> str:
    # Define the set of vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    # Convert the string to a list (strings are immutable in Python)
    s_list = list(s)
    
    # Initialize two pointers
    left, right = 0, len(s) - 1
    
    # Two pointers approach to swap vowels
    while left < right:
        # Move left pointer until we find a vowel
        if s_list[left] not in vowels:
            left += 1
        # Move right pointer until we find a vowel
        elif s_list[right] not in vowels:
            right -= 1
        # Both left and right pointers are at vowels, so swap them
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    
    # Join the list back into a string and return
    return ''.join(s_list)

# Example usage
print(reverseVowels("hello"))     # Output: "holle"
print(reverseVowels("leetcode"))  # Output: "leotcede"
