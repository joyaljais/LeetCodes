class Solution:
    def finalPrices(self, prices):

        n=len(prices)
        pr=[]

        for i in range(n):
            temp=i
            for j in range(i+1,n):
                if prices[j]<=prices[i]:
                    a=prices[i]-prices[j]
                    pr.append(a)
                    temp=j
                    break
                
            if(temp==i):
                pr.append(prices[i])

        return pr

inp=[]

no=int(input("Enter the size of array: "))

print("Enter the array elements:")
for x in range(no):
    num=int(input())
    inp.append(num)


sol=Solution()


print("Final Output", sol.finalPrices(inp))

