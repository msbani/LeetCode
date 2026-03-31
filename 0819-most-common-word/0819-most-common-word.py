class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ans = 0
        word = ""
        p=paragraph.lower()
        pattern=r'[^a-zA-Z0-9]'
        p=re.sub(pattern," ",p)
        c=Counter(p.split())
        for val,key in c.items():
            if val not in banned:
                if key > ans:
                    ans = key
                    word = val
        return word