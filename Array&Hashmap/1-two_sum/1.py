from collections import defaultdict

def twoSum(nums, target):
  for i in range(len(nums)):
    for j in range(i,len(nums)):
      if nums[i]+nums[j]==target:
        return[i,j]

 


print(twoSum([2,7,11,15],9) )     