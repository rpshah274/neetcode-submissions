from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_graph = defaultdict(list)
        indegree=[0]*numCourses

        for c,p in prerequisites:
            indegree[c]+=1
            course_graph[p].append(c)
        
        ready = deque([i for i in range(numCourses) if indegree[i] == 0])
        order=[]
        while ready:
            c=ready.popleft()
            order.append(c)
            for node in course_graph[c]:
                indegree[node]-=1
                if indegree[node]==0:
                    ready.append(node)

        return order if len(order)==numCourses else []
        
        