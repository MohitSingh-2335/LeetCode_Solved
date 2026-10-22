class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        l = []
        d = 0
        i = 0
        m = []
        while i < len(words):
            a = len(words[i])
            if d == 0 or d + 1 + a <= maxWidth:
                if d == 0:
                    d = a
                else:
                    d = d + 1 + a
                l.append(words[i])
                i += 1
            else:
                gap = len(l) - 1
                new = len("".join(l))
                ad = maxWidth - new
                s = ""
                if gap != 0:
                    f = ad // gap
                    g = ad % gap
                    for k in range(len(l) -1):
                        s += l[k]
                        s += " "*f
                        if g > 0:
                            s += " "
                            g -= 1
                    s += l[-1]
                else:
                    s += l[-1]
                    s += " "*ad
                m.append(s)
                l = []
                d = 0
        ll = " ".join(l)
        ll += " "*(maxWidth - len(ll))
        m.append(ll)
        return m
            