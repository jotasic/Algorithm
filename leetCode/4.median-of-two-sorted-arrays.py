
from typing import List 
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       
        # 두개의 List를 합친다.
        nums1.extend(nums2)
        arr = sorted(nums1)
        l = len(arr) 
        
        # List에 요소가 1개일 경우 예외처리
        if l == 1 :
            result = arr[0]
        
        # 홀수 일 경우 List에 중간 Index의 값을 접근 
        elif l % 2 == 1 :
            result = arr[int((l-1) / 2)]
            
        # 짝수일 경우 List에 존재하는 중간 2개의 Index 값을 접근
        else :
            result = (arr[int(l/2)]+arr[int(l/2-1)]) / 2        
        return result
            

        return result
        

#[0,0,0,0,0]
#[-1,0,0,0,0,0,1]




sol = Solution()
#sol.findMedianSortedArrays ([0,0,0,0,0], [-1,0,0,0,0,0,1])
print(f"Result : {sol.findMedianSortedArrays ([1,1], [1,2])}")
