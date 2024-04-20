#User function Template for python3

class Solution:
    def findPath(self, m, n):
        #define the directions and changes in row and columns indices for each direction
        directions="DLRU"
        dr=[1,0,0,-1]
        dc=[0,-1,1,0]
        result=[] #list to store valid paths
        
        def is_valid(row,col,n,maze):
            return 0<=row<n and 0<=col<n and maze[row][col]==1
            
        def explore(row,col,path,maze):
            #IF REACHED the destination ,add the path to the result
            if row==n-1 and col==n-1:
                result.append(path)
                return 
            for i in range(4):
                new_row,new_col=row+dr[i],col+dc[i]
                #checks if the new cell is valid and unvisited
                if is_valid(new_row,new_col,n,maze):
                    maze[row][col]=0 #mark current cell as visited
                    explore(new_row,new_col,path+directions[i],maze) #explore further paths
                    maze[row][col]=1 #backtrack:restore current cell
        #check if the start and end cells are unblocked 
        if m[0][0]==1 and m[n-1][n-1]==1:
            explore(0,0,"",m) #start exploring from the top-left corner
        return sorted(result)
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends