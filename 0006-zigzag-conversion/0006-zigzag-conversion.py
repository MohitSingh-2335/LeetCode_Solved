class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ss = [""]*numRows
        row = 0
        direc = 1
        i = numRows
        if numRows is 1:
            return s
        for j in range(len(s)):
            ss[row] += s[j]
            row += direc
            if row == i-1:
                direc = -1
            if row == 0:
                direc = 1
        rows = "".join(ss)
        return rows