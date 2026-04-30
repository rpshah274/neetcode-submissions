class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        adj=defaultdict(list)
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        visited=set()
        q=deque([(0,-1)])
        visited.add(0)
        while q:
            node,parent = q.popleft()
            for nei in adj[node]:
                if nei==parent:
                    continue
                if nei in visited:
                    return False
                else:
                    visited.add(nei)
                    q.append((nei,node))
        
        return len(visited)==n
