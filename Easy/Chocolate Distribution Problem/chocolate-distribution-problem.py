#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        i=0
        j=M-1
        min_di=float('inf')
        while j<N:
            curr_di=A[j]-A[i]
            min_di=min(min_di,curr_di)
            i+=1
            j+=1
        return min_di

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends