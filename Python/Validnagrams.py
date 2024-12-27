class Solution(object):
  def ValidAnagrams(self, s, t):
    if(len(s) != len(t):
      return False
    countS,countT = {},{}
    for i in s[i]:
      countS(s[i]) = 1 + countS.get(s[i],0)
      countT(s[j]) = 1 + countT.get(s[j],0)
    return countS == countT
    
      
      
  
