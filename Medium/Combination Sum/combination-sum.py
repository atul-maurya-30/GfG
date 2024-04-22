#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,A, B):
        def number(arr,B,ans,temp,index):
        # code here
            if B==0:
                ans.append(list(temp))
                return
            for i in range(index,len(arr)):
                if B-arr[i]>=0:
                    temp.append(arr[i])
                    number(arr,B-arr[i],ans,temp,i)
                    temp.remove(arr[i])
        ans=[]
        temp=[]
        arr=sorted(list(set(A)))
        number(arr,B,ans,temp,0)
        return ans
#{ 
 # Driver Code Starts.


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a,s)
        if(not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

# } Driver Code Ends