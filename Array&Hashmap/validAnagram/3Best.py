from collections import Counter
def isAnagram( s, t):

  if len(s)!= len(t):
      return False   
  return Counter(s)==Counter(t)
      


print(isAnagram("anagram","nagaram"))      