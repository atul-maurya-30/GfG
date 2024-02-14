#User function Template for python3

class Solution:

    def reverseAlternate(self, Str):
        # code here
        m=Str.split(" ")
        for i in range(1,len(m),2):
            new=m[i]
            m[i]=new[::-1]
        return " ".join(m)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        Str = input()

        solObj = Solution()

        print(solObj.reverseAlternate(Str))

# } Driver Code Ends