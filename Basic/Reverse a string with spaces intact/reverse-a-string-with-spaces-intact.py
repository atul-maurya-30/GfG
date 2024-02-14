#User function Template for python3

class Solution:
    def reverseWithSpacesIntact(self, s):
        # code here
        i=0
        j=len(s)-1
        while i<j:
            if s[i]==" ":
                i+=1
                continue
            if s[j]==" ":
                j-=1
                continue
            s=s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
            i+=1
            j-=1
        return s
    #{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.reverseWithSpacesIntact(s)
        print(ans)
# } Driver Code Ends