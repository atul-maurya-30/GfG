#{ 
 # Driver Code Starts

# } Driver Code Ends

def reverse(S):
    
    #Add code here
    S=list(S)
    stack=[]
    for i in S:
        stack.append(i)
    for i in range(len(S)):
        S[i]=stack.pop()
    return "".join(S)
    

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends