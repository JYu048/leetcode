class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       
        if not candidates: return []

        def dfs(index, path, total):
            if total == target:
                res.append(path.copy())
                return
            elif total > target or index == len(candidates):
                return
            

            path.append(candidates[index])
            dfs(index + 1, path, total + candidates[index])

            path.pop()
            while index + 1 < len(candidates) and candidates[index + 1] == candidates[index]:
                index += 1
            
            dfs(index + 1, path, total)
        
        candidates.sort()
        res = []
        dfs(0, [], 0)
        return res
