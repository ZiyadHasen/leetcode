from collections import defaultdict
def groupAnagrams(strs):
  hash_map=defaultdict(int)
  result=[]
  for str in strs:
    sorted_str=''.join(sorted(str))
    if not sorted_str in hash_map:
      hash_map[sorted_str]=len(result) 
      # !hash_map[sorted_str]= position in array where the comming unsorted value is placed 
      result.append([str])
    else:
     result[hash_map[sorted_str]].append(str)


  return result



print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))