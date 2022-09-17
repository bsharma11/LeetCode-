class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        backward, res = {}, []
        for i, word in enumerate(words):
            backward[word[::-1]] = i

        for i, word in enumerate(words):
            if word in backward and backward[word] != i:                
                res.append([i, backward[word]])
                
            if word != "" and "" in backward and word == word[::-1]:
                res.append([i, backward[""]])
                res.append([backward[""], i])
                
            for j in range(len(word)):
                
                if word[j:] in backward and word[:j] == word[j-1::-1]:
                
                    res.append([backward[word[j:]], i])
                if word[:j] in backward and word[j:] == word[:j-1:-1]:

                    res.append([i, backward[word[:j]]])
                    
        return res
    
#     MY CODE(not optimised)
#         def isPalindrome(s):
#             i = 0
#             j = len(s)- 1
#             while i < j:
#                 if s[i] == s[j]:
#                     i += 1
#                     j -= 1
#                 else:
#                     return False
#             return True
#         b = []
#         for i in range(len(words)):
#             if words[i] == "":
#                 for j in range(i+1,len(words)):
#                     if isPalindrome(words[j]):
#                         b.append([i,j])
#                         b.append([j,i])
#             else:
#                 for j in range(i+1,len(words)):
#                     if words[j] =="":
#                         if isPalindrome(words[i]):
#                             b.append([i,j])
#                             b.append([j,i])
#                     else:
#                         x = words[i] + words[j]
#                         y = words[j] + words[i]
#                         if isPalindrome(x):
#                             b.append([i,j])
#                         if isPalindrome(y):
#                             b.append([j,i])
                            
#         return (b)