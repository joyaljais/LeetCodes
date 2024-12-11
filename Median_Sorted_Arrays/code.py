class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()

        n=len(nums3)

        if n % 2 != 0:
            return float(nums3[int(n/2)])

        else:
 
            return float((nums3[int((n-1)/2)] + nums3[int(n/2)])/2.0)
 



arr1=input("Enter sorted array [1]: ").split()
arr2=input("Enter sorted array [2]: ").split()

sol=Solution()


sol.findMedianSortedArrays(arr1,arr2)

