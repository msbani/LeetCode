class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == "R":
                R.append(i)
            else:
                D.append(i)
        while R and D:
            dire = D.popleft()
            radiant = R.popleft()
            if dire < radiant:
                D.append(dire + n)
            else:
                R.append(radiant + n)
        return "Radiant" if R else "Dire"
