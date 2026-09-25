class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        rev=0
        if x <0:
            return False
        while x>0:
          d = x%10
          x=x//10
          rev =(rev*10)+d
        if n == rev:
            return True
        else:
            return False

        