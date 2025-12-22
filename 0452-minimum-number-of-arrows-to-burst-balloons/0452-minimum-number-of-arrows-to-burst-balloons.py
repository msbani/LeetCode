class Solution:
    def findMinArrowShots(self, points:List[List[int]])->int:
        points.sort(key = lambda x: x[1])
        pop = points[0][1]
        arrow = 1   
        for start, end in points:
            if start > pop:
                arrow += 1
                pop = end
        return arrow 

# Another Solution
        # points.sort()
        # res = len(points)
        # prev = points[0]
        # for i in range(1, len(points)):
        #     curr = points[i]
        #     if curr[0] <= prev[1]:
        #         res -= 1
        #         prev = [curr[0], min(curr[1], prev[1])]
        #     else:
        #         prev = curr
        # return res