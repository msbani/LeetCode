class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain = [0] + gain
        max_alt = 0
        
        for i in range(len(gain)):
            alt = max_alt + gain[i]
            max_alt = alt
            gain[i] = max_alt
        return max(gain)
