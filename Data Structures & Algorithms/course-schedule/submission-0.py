class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre=defaultdict(list)
        for c,p in prerequisites:
            pre[c].append(p)
        visit=set()
        def dfs(course):
            if not pre[course]:
                return True
            if course in visit:
                return False
            visit.add(course)
            for p in pre[course]:
                if not dfs(p):
                    return False
            visit.remove(course)
            pre[course]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True