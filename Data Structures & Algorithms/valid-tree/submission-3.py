class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > (n - 1):
            return False

        adjList = {i : [] for i in range(n)}
        visited = set()

        for src, dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)
        
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)

            for j in adjList[i]:
                if j == prev:
                    continue

                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
        