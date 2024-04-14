#User function Template for python3

class Solution:

    def findPair(self, arr,n,diff):
        arr.sort()
        left, right = 0, 1
        while right < L:
            diff = arr[right] - arr[left]
            if diff == N:
                return True
            elif diff < N:
                right += 1
            else:
                left += 1
                if left == right:
                    right += 1
        return False




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        L,N = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        if(solObj.findPair(arr,L, N)):
            print(1)
        else:
            print(-1)
# } Driver Code Ends