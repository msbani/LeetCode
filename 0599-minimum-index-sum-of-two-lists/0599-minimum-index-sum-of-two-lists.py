class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)
        index_sum = {}
        for i, r in enumerate(list1):
            if r in common:
                index_sum[r] = i
        for i, r in enumerate(list2):
            if r in common:
                index_sum[r] += i
        min_sum = min(index_sum.values())
        return [r for r, s in index_sum.items() if s == min_sum]

        """ans = []
        min_index_sum = float(inf)
        for i in range(len(list1)):
            if list1[i] in list2:
                j = list2.index(list1[i])
                if i + j < min_index_sum:
                    min_index_sum = i + j
                    ans = [list1[i]]
                elif i + j == min_index_sum:
                    ans.append(list1[i])
        return ans"""