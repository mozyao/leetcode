from typing import List


class Solution:
    
    
    def dfs(self,row:int,col:int,visited:set,grid: List[List[int]]) -> int:
            
            if not (0<= row < len(grid) and 0<=col < len(grid[0]) and
                    (row,col) not in visited and
                    grid[row][col] ):
                
                    # make sure the pos of this spot grid[row][col] is inside and havn't beed visited before and it's value is 1
                return 0
            visited.add((row,col)) # log every visited spot
            return (1+ self.dfs(row+1,col,visited,grid) +self.dfs(row,col+1,visited,grid)
                     + self.dfs(row-1,col,visited,grid) + self.dfs(row,col-1,visited,grid)  )
         # if its a valid spot([1]) , expand towards 4 directions and add upon all 1's 
        # then we get the area of any island related to this spot
    
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # iterate all sopts in the grid
        visited = set()
        
        return max( self.dfs(r,c,visited,grid)
                    for r in range(len(grid))
                    for c in range(len(grid[0])))

                


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]


if __name__ == "__main__":
    ans = Solution()

    print(ans.maxAreaOfIsland(grid))
