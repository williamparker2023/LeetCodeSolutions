"""
Hard

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

https://leetcode.com/problems/distinct-subsequences/description/
"""

"""
Even though the "Hard DP" status can be intimidating, this problem is acually quite straightforward
once you've done a few DP problems. Basically, the idea is that we want a 2D DP table where each cell
dp[i][j] represents the number of distinct subsequences of s[:j] that fit up to t[:i].

at each i,j, our optimal amount is either the amount at dp[i][j-1] if s[j]!=t[i], or
dp[i][j-1] + dp[i-1][j-1]  if s[j]==t[i]. The though here is that if the current letters are
different, then adding the most recent letter to s did nothing to help us get more ways of matching t,
meaning that the optimal amount would be the same as if we went to the previous letter in t.
If they are the same though, we could either choose adding the current letter to the end of t,
or adding the current letter to s and t. An "or" in dp ususally means adding, so we just add the
i,j-1 and i-1,j-1 answers together for our current i,j answer.

Finally, we don't actually need the whole 2D table, just a current and previous row.
This gives us O(n) space, and O(mn) time complexity.
"""

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        prev = [1]*(len(s)+1)

        for i in range(1,len(t)+1):
            cur = [0]*(len(s)+1)
            for j in range(1,len(s)+1):
                if t[i-1] == s[j-1]:
                    cur[j] = cur[j-1] + prev[j-1]
                elif j>=i:
                    cur[j] = cur[j-1]
            prev = cur
        return prev[-1]