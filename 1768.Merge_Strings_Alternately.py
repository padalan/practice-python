"""
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  abc
word2:  pqr
merged: apbqcr

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  ab 
word2:  pqrs
merged: apbqrs

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  abcd
word2:  pq 
merged: apbqcd

Constraints:

    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.
"""

def mergeAlternately(word1, word2):
    # Initialize merged string
    merged = []
    
    # Find the minimum length of the two strings
    min_length = min(len(word1), len(word2))
    
    # Merge alternating characters from both strings
    for i in range(min_length):
        merged.append(word1[i])
        merged.append(word2[i])
    
    # Append the remaining characters from the longer string
    if len(word1) > len(word2):
        merged.append(word1[min_length:])
    else:
        merged.append(word2[min_length:])
    
    # Join the list into a single string and return
    return ''.join(merged)

# Example usage
print(mergeAlternately("abc", "pqr"))  # Output: "apbqcr"
print(mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"
print(mergeAlternately("abcd", "pq"))  # Output: "apbqcd"
