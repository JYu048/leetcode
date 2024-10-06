class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def getCombs(path, index):
            if len(path) == len(digits):
                path = "".join(path)
                res.append(path)
                return
            
            letters = numToLetter[digits[index]]
            for letter in letters:
                path.append(letter)
                getCombs(path, index + 1)
                path.pop()
        

        if not digits: return []

        numToLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        getCombs([], 0)
        return res