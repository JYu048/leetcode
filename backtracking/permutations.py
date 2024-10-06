class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(path, visited):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            # Explore paths
            for i in range(len(nums)):
                # i is already in path
                if visited[i]:
                    continue
                
                # add i to path and mark as seen
                path.append(nums[i])
                visited[i] = True
                dfs(path, visited)

                # remove i and mark it as unseen 
                path.pop()
                visited[i] = False
        
        if not nums: return []
        res = []
        dfs([], [False] * len(nums))
        return res
        
