class Solution(object):
    def lengthOfLIS(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        LIS_length = 1
        dp = [1]*len(s)
        for i in range(1, len(s)):
            for j in range(0, i):
                if s[i] > s[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            LIS_length = max(dp[i], LIS_length)
        return LIS_length