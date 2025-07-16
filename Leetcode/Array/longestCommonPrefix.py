# 14. Longest Common Prefix
# Solved
# Easy
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        store = [] 
        rem = []
        found = False
        if not strs:
            return ""

        for i in strs:
            letter = list(i)
            store.append(letter)

        min_len = min(len(word) for word in store)

        for char_index in range(min_len):
            current_char = store[0][char_index]
            for word_index in range(1, len(store)):
                if store[word_index][char_index] != current_char:
                    found = True
                    break
            if found:
                break
            rem.append(current_char)

        if rem:
            return ''.join(rem)
        else:
            return ""
# This function finds the longest common prefix string among a list of strings.
# 
# Steps:
# 1. Converts each input string into a list of characters and stores them in `store`.
# 2. Determines the minimum length among all strings to avoid index errors.
# 3. Iterates character by character (column-wise) across all strings:
#    - Compares the current character from the first word with the same-position character in all other words.
#    - If all match, the character is part of the prefix and added to `rem`.
#    - If a mismatch is found, breaks out of the loops.
# 4. Joins and returns the collected prefix characters as a single string.
# 5. Returns an empty string if no common prefix exists or input list is empty.

'''
Accepted
126 / 126 testcases passed
priyanshvermaofficial
priyanshvermaofficial
submitted at Jul 16, 2025 22:01

Editorial

Solution
Runtime
0
ms
Beats
100.00%
Analyze Complexity
Memory
18.04
MB
Beats
8.36%
Analyze Complexity
'''
