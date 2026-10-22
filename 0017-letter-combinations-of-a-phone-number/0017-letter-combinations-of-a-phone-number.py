class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dig = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        count = []
        for i in digits:
            if i in dig.keys():
                count.append(dig[i])
                if len(digits) == 1:
                    return dig[i]
            else:
                pass

        j = count[0]
        for mat in count[1:]:
            final = []
            for m in j:
                for n in mat:
                    final.append(m + n)

            j = final

        return final 