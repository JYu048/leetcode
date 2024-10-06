class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        def dfs(index, path, total):
            if total == target:
                res.append(path.copy())
                return
            elif total > target or index == len(candidates):
                return
            
            
            path.append(candidates[index])
            # don't add to index. This way same element can be added multiple times, as long as it's smaller than target
            dfs(index, path, total + candidates[index])
        
            path.pop()
            dfs(index + 1, path, total)
            
        res = []
        dfs(0, [], 0)
        return res
            
        