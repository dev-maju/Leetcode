class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        
        row, col = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                rows, cols = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r, c = rows + dr, cols + dc
                    if (r in range(row) and
                        c in range(col) and
                        grid[r][c] == '1' and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    islands +=1
        
        return islands