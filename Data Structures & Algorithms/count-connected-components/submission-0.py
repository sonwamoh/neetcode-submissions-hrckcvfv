class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        adj_list = {i : [] for i in range(n)}
        visited = set()

        def dfs(i):
            visited.add(i)

            for j in adj_list[i]:
                if j not in visited:
                    dfs(j)
            
            return

        for dst, src in edges:
            adj_list[dst].append(src)
            adj_list[src].append(dst)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count

        