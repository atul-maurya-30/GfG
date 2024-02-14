#User function Template for python3

class Solution:
    def isSpecialChar(self,char):
        return not char.isalnum()
    def reverse(self, s):
        # code here
        s=list(s)
        stack=[]
        for i in s:
            if not self.isSpecialChar(i):
                stack.append(i)
        for i in range(len(s)):
            if not self.isSpecialChar(s[i]):
                s[i]=stack.pop()
        return "".join(s)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        ans = ob.reverse(s)
        print(ans)
# } Driver Code Ends