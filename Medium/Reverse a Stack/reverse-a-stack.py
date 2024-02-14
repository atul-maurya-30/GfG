#User function Template for python3

from typing import List

class Solution:
    def reverse(self,St): 
        #code here
        stack=[]
        for i in St:
            stack.append(i)
        for i in range(len(St)):
            St[i]=stack.pop()
        return St[i]


#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends