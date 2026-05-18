from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # key: node, val: list [neighbours of the node]
        # It's bidirectional graph
        # visited set = set()
        # number of conected componenets = numbers of time we do bfs on the node
        # that's not in the visited set
        # TC: O(n*m), SC: O(n*m), n is num of edges, m is num of vertexes

        adjList = defaultdict(list) 

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        visited = set()
        q = deque([])
        cnt = 0

        def bfs(node):
            q.append(node)
            visited.add(node)

            # n = 5, edges = [[0,1],[1,2],[3,4]]

            """
            q = []
            visited = [0, 1, 2]
            curr = 2
            adjList[2] 
                nei 1
            """

            while q:
                curr = q.popleft()
                for nei in adjList[curr]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
                    else:
                        continue


        for node, _ in adjList.items():
            if node not in visited:
                bfs(node)
                cnt += 1
        
        return cnt



        