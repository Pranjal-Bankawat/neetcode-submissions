class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNum = "".join(ch.lower() for ch in s if ch.isalnum())
        first = 0
        last = len(alphaNum)-1
        
        while last > first:
            if alphaNum[first] == alphaNum[last]:
                first += 1
                last -= 1
            else:
                return False
        return True
