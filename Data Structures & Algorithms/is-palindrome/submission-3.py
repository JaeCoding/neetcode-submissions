class Solution:
    def isAlphaOrNumber(self, s: str) -> bool:
        return s.isalpha() or s.isdigit()

    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        l_point = 0
        r_point = len(s) - 1
        while True:
            # when l_point move to r_point right
            if l_point >= r_point:
                return True   
            while not self.isAlphaOrNumber(s[l_point]) and l_point < len(s) - 1:
                l_point += 1
            while not self.isAlphaOrNumber(s[r_point]) and r_point > 0:
                r_point -= 1    
            print(s[l_point] + '_' + s[r_point])       
            if l_point >= r_point:
                return True 
            if s[l_point] != s[r_point]:
                return False
            l_point += 1
            r_point -= 1






        