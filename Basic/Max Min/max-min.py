class Solution:
    def findSum(self,A,N): 
        #code here
        mina=min(A)
        maxa=max(A)
        return(maxa+mina)

#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends