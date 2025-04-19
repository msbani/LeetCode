class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        maxPoints = 0
        for p1, p2 in combinations(points, 2):
            count = 0
            for p in points:
                if (p[1] - p1[1]) * (p2[0] - p1[0]) == (p[0] - p1[0]) * (p2[1] - p1[1]):
                    count += 1
            maxPoints = max(maxPoints, count)
        return maxPoints