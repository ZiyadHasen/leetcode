from collections import defaultdict
def groupAnagrams(strs):
# * the main takeaway here is may be this , the key must be int not array , but the default value 
# *can be anything including array

  hash_map=defaultdict(list)
  for str in strs:
    sorted_str=''.join(sorted(str))
    hash_map[sorted_str].append(str)


  return list(hash_map.values())



print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))