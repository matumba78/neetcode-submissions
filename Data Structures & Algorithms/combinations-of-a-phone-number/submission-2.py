class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def dfs(i, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return 
            
            for c in char_map[digits[i]]:
                dfs(i + 1, curr_str + c)
        
        if digits:
            dfs(0, "")
        return res
        
            
        
                
        