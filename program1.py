from collections import deque
def numIsIands(grid):
   if not grid:
      return 0

   def bfs(grid,i,j):
      queue=deque([(i, j)])
      grid[i][j]='W'

      directions=[(0,1),(0,-1),(1,0),(-1,0)]
      while queue:
         x,y =queue.popleft()
         for dx, dy in directions:
            nx,ny=x+dx, y+dy

         if 0<=nx <len(grid) and 0 <=ny <len(grid[0]) and grid[nx][ny]=='L':
            grid[nx][ny]='W'
            queue.append((nx,ny))

num_islands=0
for i in range(len(grid)):
   for j in range(len(grid[0])):
      if grid[i][j]=='L':
         num_islands +=1
         bfs(grid,i,j)

return num_islands
