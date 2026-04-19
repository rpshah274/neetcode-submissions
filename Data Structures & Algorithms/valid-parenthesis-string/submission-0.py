class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        stack=[]
        star_stack=[]
        for i in range(n):
            ch=s[i]
            if ch=='(':
                stack.append(i)
            if ch==')':
                if stack:
                    stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            if ch=='*':
                star_stack.append(i) 
        while stack and star_stack:
            if stack[-1] < star_stack[-1]:
                stack.pop()
                star_stack.pop()
            else:
                return False
        return not stack