class Solution(object):
  def containsDuplicate(self,nums):
    hashSet = set()
    for n in nums:
      if n in hashSet:
        return True
      hashSet.add(n)
    return False
