def twoSum(nums, target):
    res=[]
    for x in range(len(nums)):
        for y in range(x,len(nums)):
            if(nums[x]+nums[y]==target):
                
                res.append(x)
                res.append(y)
                exit
        # if(len(res)!=0):
        #     break
        

    print(res)
                
                    

input_str = input("Enter elements of the list separated by space: ")  
  
# Converting input string to a list of integers  
nums = input_str.split()  
nums = [int(num) for num in nums]  
  
# Printing the list  
print("List:", nums)

target=int(input("Enter sum:"))
twoSum(nums, target)