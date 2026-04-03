from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = numCourses * [0]

        for a, b in prerequisites:
            inDegree[a] += 1
            graph[b].append(a)
        
        queue = deque()

        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        taken = 0
        while queue:
            node = queue.popleft()
            taken += 1

            for nei in graph[node]:
                inDegree[nei] -= 1
                
                if inDegree[nei] == 0:
                    queue.append(nei)

        return taken == numCourses
        