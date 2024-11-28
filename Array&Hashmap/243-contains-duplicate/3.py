from collections import defaultdict
from collections import Counter
def containsDuplicate( nums):
  hash=Counter(nums)
  for value in hash.values():
    if value>1:
      return True

    else:
      return False
  
  
  # print(hash.items())  
  
print(containsDuplicate([1,2,3,1]))




# this also work
#  def containsDuplicate(self, nums):
#         nums=sorted(nums)
#         #1123

#         for i in range(len(nums)-1):
#             if nums[i]==nums[i+1]:
#                 return True
#         return False  