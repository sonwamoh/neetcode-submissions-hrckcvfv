"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Dict, Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        # dict to map old to copy
        clone: Dict[Node, Node] = {}
        clone[node] = Node(node.val)
        # append the 1st node
        queue = deque([node])

        while queue:
            # curr node
            curr = queue.popleft()       
            # itr ovr nei of curr
            for nei in curr.neighbors:
                # create copy for those not in clones
                if nei not in clone:
                    # copy add to map
                    clone[nei] = Node(nei.val)
                    queue.append(nei)
                # nei of clone node updated
                clone[curr].neighbors.append(clone[nei])
            
        return clone[node]
                





        # def dfs(node):
        #     if node in clones:
        #         return clones[node]
            
        #     # we are creating a copy over here
        #     copy = Node(node.val)
        #     # mapping node -> copy
        #     clones[node] = copy

        #     for nei in node.neighbors:
        #         # add nei to copy
        #         copy.neighbors.append(dfs(nei))
        #     return copy
        
        # return dfs(node)

        
        