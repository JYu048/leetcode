class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def backtrack(index):
            if index == len(s):
                res.append(partition[:])
                return
            
            for end in range(index, len(s)):
                if isPalindrome(index, end):
                    partition.append(s[index:end+1])
                    backtrack(end + 1)
                    partition.pop()
        
        
        def isPalindrome(left, right):

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1
            
            return True

        res = []
        partition = []
        backtrack(0)
        return res