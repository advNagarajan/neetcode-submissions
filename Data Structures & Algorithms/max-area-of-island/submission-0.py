class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        max_area = 0

        def bfs(r, c):
            area = 1
            q = collections.deque([(r, c)])
            visit.add((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = row + dr, col + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visit
                    ):
                        visit.add((nr, nc))
                        q.append((nr, nc))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = bfs(r, c)
                    max_area = max(max_area, area)
                    print(max_area)

        return max_area