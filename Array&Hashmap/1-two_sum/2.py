from collections import defaultdict

def twoSum(nums, target):
  hash_map=defaultdict(int)
  for i,num in enumerate(nums):
    compliment=target-num
    if compliment in hash_map:
      return [hash_map[compliment],i]
    hash_map[num]=i

   

print(twoSum([2,7,11,15],9) )  


