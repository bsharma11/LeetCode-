class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
            ans = [] 
			#answer storing array
            
			#when we need to return vacant array
            if len(changed)%2:
                    return ans
					#when we will have odd number of integer in our input(double array can't be in odd number)
    
            changed.sort()
			#sorting 

            temp = Counter(changed)
			#storing the frequencies
            for i in changed:    
                if temp[i] == 0:  
				#if we have already decreased it's value when we were checking y/2 value, like 2,4 we will remove 4 also when we                    will check 2 but our iteration will come again on 4.
      
                    continue
                else:
                    if temp.get(2*i,0) >= 1:
					#if we have both y and y*2, store in our ans array
                        ans.append(i)
						#decrease the frequency of y and y*2
                        temp[2*i] -= 1
                        temp[i] -= 1
                    else:        
                        return []
            return ans
        # changed.sort()
        # def naya(a,i):
        #     for j in range(i+1,len(a)):
        #         if a[j] == 2*a[i]:
        #             a[j] = None
        #             return a
        #     else:
        #         return []
        # if len(changed) == 1 or len(changed) %2 != 0:
        #     return []
        # b = []
        # i = 0
        # while i < len(changed):
        #     if changed[i] == None:
        #         i += 1
        #         continue
        #     changed = naya(changed,i)
        #     if changed == []:
        #         return [] 
        #     b.append(changed[i])
        #     i+=1
        # if len(b) != len(changed)//2:
        #     return []
        # else:
        #     return b