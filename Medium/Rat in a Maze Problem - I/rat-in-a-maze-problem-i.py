#User function Template for python3

class Solution:
    def findPath(self, m, n):
        directions = "DLRU"
        dr = [1, 0, 0, -1]
        dc = [0, -1, 1, 0]

        def is_valid(row, col, n, maze):
            return 0 <= row < n and 0 <= col < n and maze[row][col] == 1

        def explore(row, col, maze, path, all_paths, m, n):
            if row == m - 1 and col == n - 1:
                all_paths.append(path)
                return

            maze[row][col] = 0

            for i in range(len(directions)):
                new_row, new_col = row + dr[i], col + dc[i]
                if is_valid(new_row, new_col, m, maze):
                    explore(new_row, new_col, maze, path + directions[i], all_paths, m, n)

            maze[row][col] = 1

        result = []
        if m[0][0] == 1 and m[n - 1][n - 1] == 1:
            explore(0, 0, m, '', result, len(m), len(m[0]))

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