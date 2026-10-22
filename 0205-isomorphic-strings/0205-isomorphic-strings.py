from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a = 0
        if len(list(s)) != len(list(t)):
            return False
        mapp = defaultdict(list)
        imap = defaultdict(list)
        for k, v in zip(s, t):
            mapp[k].append(v)
        for k, v in zip(s, t):
            imap[v].append(k)
        for k, v in mapp.items():
            if len(set(v)) > 1:
                a += 1
        for k, v in imap.items():
            if len(set(v)) > 1:
                a += 1
        if a > 0:
            return False
        else:
            return True