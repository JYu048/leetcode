class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(index, path):
            if index > len(nums) - 1:
                res.append(path.copy())
                return
            
            dfs(index + 1, path + [nums[index]]) # include
            dfs(index + 1, path) # exclude
        
        if not nums: return []
        
        res = []
        dfs(0, [])
        return res
        