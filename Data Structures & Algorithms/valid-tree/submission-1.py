class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for a, b in edges:
                neighbor = None
                if a == node and b != parent:
                    neighbor = b
                elif b == node and a != parent:
                    neighbor = a

                if neighbor is not None:
                    if not dfs(neighbor, node):
                        return False
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n
