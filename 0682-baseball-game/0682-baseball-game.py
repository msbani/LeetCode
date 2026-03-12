class Solution:
    def calPoints(self, operations: List[str]) -> int:
        cur_score = 0
        stack = []
        for i in operations:
            if i == '+':
                a = stack[-2] + stack[-1]
                stack.append(a)
                cur_score += a
            elif i == 'C':
                cur_score -= stack.pop()
            elif i == 'D':
                t = stack[-1] * 2
                cur_score += t
                stack.append(t)
            else:
                stack.append(int(i))
                cur_score += int(i)
        return cur_score
        