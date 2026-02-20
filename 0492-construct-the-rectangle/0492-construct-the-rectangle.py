class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        length = 0
        breadth = int(math.sqrt(area))
        while area % breadth != 0:
            breadth -= 1
        length = area // breadth
        return [length, breadth]