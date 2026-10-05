class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        rev=0
        while x>0 :
            r=x%10
            x=x//10
            rev=rev*10+r
        if rev==num:
            return True
        else:
            return False 

