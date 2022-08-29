https://www.youtube.com/watch?v=8ftRiPafAjk&ab_channel=ADev%27Story

https://www.youtube.com/watch?v=DIR_rxusO8Q&ab_channel=FullstackAcademy

1. Repeat: make sure you do understand the problem. 
2. Example: get insights by doing examples 
3. Approach: come up with your approach(es) to the problem (brute force first) 
4. Code: write the code for your chosen approach 
5. Testing: pass the test cases 
6. Optimize: optimize the complexities (time and space) of your algorithm

https://www.softwaretestinghelp.com/coding-interview-questions/

Data Structures and Algorithms

Leetcode

https://leetcode.com/problems/number-of-islands/

```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) # find side length of the grid/matrix
        visited = [[False] * n for _ in range(m)]  # in m x n check if the cell have been visited in the dfs
        
        def dfs(x,y):
            if visited[x][y]: 
                return
            visited[x][y] = True # set this cell to True as you just visited it
            for new_x,new_y in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)): # check top, left, right, and bottom cells
                if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or grid[new_x][new_y] == "0": # if they are not out of the border, 
                    continue
                dfs(new_x,new_y)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i,j)
                    ans += 1
        return ans
        ```
