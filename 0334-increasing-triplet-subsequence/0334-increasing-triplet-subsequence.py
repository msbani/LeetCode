# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         first = second = float('inf')
#         for n in nums:
#             if n <= first:
#                 first = n
#             elif n <= second:
#                 second = n
#             else:
#                 return True
#         return False

class Solution:
    def increasingTriplet(self, nums:List[int]) -> bool:
        i = j = float("inf")

        for n in nums:
            if n <= i:
                i = n
            elif n <= j:
                j = n
            else:
                return True
        return False


