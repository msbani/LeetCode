class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)

        for n in arr:
            d[n] += 1
        count = list(d.values())

        return len(count) == len(set(count))



