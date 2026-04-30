class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #DFS
        if len(edges) > (n-1):
            return False
        adj=defaultdict(list)
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        visited=set()

        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei==parent:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        return dfs(0,-1) and len(visited)==n
        #BFS
        # q=deque([(0,-1)])
        # visited.add(0)
        # while q:
        #     node,parent = q.popleft()
        #     for nei in adj[node]:
        #         if nei==parent:
        #             continue
        #         if nei in visited:
        #             return False
        #         else:
        #             visited.add(nei)
        #             q.append((nei,node))
        
        # return len(visited)==n
