#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        if len(S)<=1:
            return S
        result=S[0]
        for i in range(1,len(S)):
            if S[i]!=S[i-1]:
                result+=S[i]
        return result
        
        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends