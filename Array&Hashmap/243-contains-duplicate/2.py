from collections import defaultdict
def containsDuplicate( nums):
  hash=defaultdict(int)
  for n in nums:
    hash[n]+=1
  if any(value > 1 for value in hash.values()):
    return True
  else:
    return False
  
  
  # print(hash.items())  
  
print(containsDuplicate([1,2,3,1]))