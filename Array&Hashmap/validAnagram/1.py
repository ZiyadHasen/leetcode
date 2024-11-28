def isAnagram( s, t):
      sorted_t=sorted(t)
      sorted_s=sorted(s)

      if len(sorted_t)==len(sorted_s):
          if sorted_t==sorted_s:
            return True
          else:
            return False    


      else:
        return False   
      


print(isAnagram("anagram","nagaram"))      