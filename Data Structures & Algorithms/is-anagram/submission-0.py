class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for ct in t:
            if ct not in counts:
                return False
            counts[ct] -= 1
            if counts[ct] < 0:
                return False
        return True              
