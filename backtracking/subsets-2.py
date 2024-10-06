class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
       

        def dfs(index, path):
            if index == len(nums):
                res.append(path.copy())
                return
            
            path.append(nums[index])
            dfs(index + 1, path)

            path.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            
            dfs(index + 1, path)
        
        nums.sort()
        res = []
        dfs(0, [])
        return res
