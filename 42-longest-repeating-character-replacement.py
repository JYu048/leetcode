from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = min(len(s), k+1)
        curr = 0  # Tracks current streak
        hashmap = defaultdict(int) # Tracks count of each char in sliding window
        left = 0
        max_freq = 0
        
        for i, char in enumerate(s):
            
            hashmap[char] += 1
            curr = i - left + 1
            max_freq = max(max_freq, hashmap[char])

            while curr - max_freq > k:
                hashmap[s[left]] -= 1
                left += 1
                curr -= 1


            
            res = max(res, curr)
        
        return res
    