class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(i):
            if i==n:
                return True

            if i in memo:
                return memo[i]

            for j in range(i+1,n+1):
                if s[i:j] in wordSet and dfs(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)
        