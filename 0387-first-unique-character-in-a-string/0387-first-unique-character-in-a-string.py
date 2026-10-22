class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dic = {}
        non = []
        i = 0

        for i in list(s):

            if i not in non:

                if i not in dic:

                    dic[i] = s.index(i)

                elif i in dic:

                    non += i
                    del dic[i]

        if len(dic) == 0:

            return -1

        return (list(dic.values())[0])
