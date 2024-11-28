
def isAnagram( s, t):

    sorted_str1=''.join(sorted(s))
    sorted_str2=''.join(sorted(t))
    return sorted_str1==sorted_str2   
      


print(isAnagram("anagram","nagaram"))      


















