from collections import defaultdict
def containsDuplicate( nums):
  hash=set()
  for n in nums:
    if n in hash:
      return True
    hash.add(n)
  return False


  
  
  # print(hash.items())  
  
print(containsDuplicate([1,2,3,1]))