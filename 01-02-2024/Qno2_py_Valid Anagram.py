'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        d1={}
        if(len(s)!=len(t)):
            return(False)
        for i in s:
            if i not in d:
                d[i]=1 
            else:
                d[i]+=1 
        for j in t:
            if j not in d1:
                d1[j]=1 
            else:
                d1[j]+=1
        for i in s:
            if i not in t:
                return(False)
            if(d[i]!=d1[i]):
                return(False)
        return(True)
