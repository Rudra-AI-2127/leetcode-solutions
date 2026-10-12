"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        d = {}
        def dfs(n):
            if n in d:
                return d[n]
            d[n] = Node(n.val)
            d[n].neighbors = [dfs(x) for x in n.neighbors]
            return d[n]
        return dfs(node)
        
        