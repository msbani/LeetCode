class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt_dic = Counter(text)
        cnt = 0
        while True:
            for x in 'balloon':
                cnt_dic[x] -= 1
                if cnt_dic[x] < 0:
                    return cnt
                    
            cnt += 1
        return cnt