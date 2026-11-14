class Solution:
    def isPalindrome(self, s: str) -> bool:
        nstr=""
        for i in s:
            if i.isalnum():
                nstr+=i.lower()
           
        rstr=''.join(reversed(nstr))
        return rstr==nstr