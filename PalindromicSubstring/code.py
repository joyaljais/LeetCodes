class Solution:
    def longestPalindrome(self, s: str) -> str:
        s=str(s)

        pali=s[0]
        
        if(s==s[::-1]):
            return s
        
        else:
            n=len(s)

            for i in range(n):
                for j in range(i+1,n+1):
                    st=s[i:j]

                    if(st==st[::-1]):
                        if(len(st)>len(pali)):
                            pali=st

            return pali
                


sol=Solution()


wor=input("Enter value: ")

print(sol.longestPalindrome(wor))

