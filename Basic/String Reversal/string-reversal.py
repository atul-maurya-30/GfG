#User function Template for python3

class Solution:
    def reverseString(self, s):
        # code here
        S=s.split()
        c="".join(S)
        reverse=c[::-1]
        b=[]
        for i in reverse:
            if i not in b:
                b.append(i)
        return "".join(b)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        ans = ob.reverseString(s)
        print(ans)
# } Driver Code Ends