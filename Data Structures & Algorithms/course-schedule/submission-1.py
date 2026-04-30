from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_graph = defaultdict(list)
        indegree = [0] * numCourses

        # build graph + indegree
        for c, p in prerequisites:
            course_graph[p].append(c) #doing this prerequisite p will unlock the course c
            indegree[c] += 1

        # start with nodes having 0 indegree
        ready_courses  = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        processed = 0

        while ready_courses :
            c = ready_courses.popleft()
            processed+=1
            for node in course_graph[c]:
                indegree[node] -= 1
                if indegree[node]==0:
                    ready_courses.append(node)
        return processed == numCourses
                   
        # def dfs(course):
        #     if not pre[course]:
        #         return True
        #     if course in visit:
        #         return False
        #     visit.add(course)
        #     for p in pre[course]:
        #         if not dfs(p):
        #             return False
        #     visit.remove(course)
        #     pre[course]=[]
        #     return True
        # for c in range(numCourses):
        #     if not dfs(c):
        #         return False
        # return True