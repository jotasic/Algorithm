class Solution:
    def longestPalindrome(self, s: str) -> str:
        strRev = reversed(s)

        l = len(s)
        resultStr =""


        for i in range(l) :
            if s[i] == s[l-i-1] :
                resultStr += s[i]
            else :
                resultStr += " "

        listStr = resultStr.split(" ")

        sorted(listStr, key=lambda listStr: len(listStr), reverse=True)


        return listStr[0]





sol = Solution()
sol.longestPalindrome("TEST")