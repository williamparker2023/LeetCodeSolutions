"""
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t 
(including duplicates) is included in the window. If there is no such substring, 
return the empty string "".

The testcases will be generated such that the answer is unique.
"""

"""
My thought process here was that we basically just want two maps.
One contains the required letters and there counts from t
The other contains our currents letters in the current sliding window in s
If the tmap is contained within our current smap, then our current substring is valid
Thus, if it's length is shorter than the current answer, make it the new current answer
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def contains(map1,map2):
            for key in map1:
                if key not in map2 and map1[key]!=0:
                    return False
                if map1[key]>map2[key]:
                    return False
            return True
        
        if len(t)>len(s):
            return ""
        
        smap = {}
        tmap = {}

        for let in t:
            if let not in tmap:
                tmap[let]=0
            tmap[let]+=1
        
        l = 0
        r = 1
        smap[s[0]] = 1

        ans = s + "a"

        while r<len(s)+1:
            if contains(tmap,smap):
                if len(ans)>r-l:
                    ans = s[l:r]
                smap[s[l]]-=1
                l+=1
            elif r<len(s):
                if s[r] not in smap:
                    smap[s[r]] = 0
                smap[s[r]]+=1
                r+=1
            else:
                break
        
        if len(ans)==len(s)+1:
            return ""
        return ans

myGuy = Solution()
print(myGuy.minWindow("abeecdabec","abc"))