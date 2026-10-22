class Solution:
    def intToRoman(self, num: int) -> str:
        tho = {1:"M",2:"MM",3:"MMM"}
        hun = {1:"C",2:"CC",3:"CCC",4:"CD",5:"D",6:"DC",7:"DCC",8:"DCCC",9:"CM"}
        ten = {1:"X",2:"XX",3:"XXX",4:"XL",5:"L",6:"LX",7:"LXX",8:"LXXX",9:"XC"}
        one = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
        rom = ""
        nums = str(num)
        numss = list(nums)
        n = []
        for i in numss:
            n.append(int(i))
        a = len(n)
        if a == 1:
            if n[0] in one.keys():
                rom += one[n[0]]
        if a == 2:
            if n[0] in ten.keys():
                rom += ten[n[0]]
            if n[1] in one.keys():
                rom += one[n[1]]
        if a == 3:
            if n[0] in hun.keys():
                rom += hun[n[0]]
            if n[1] in ten.keys():
                rom += ten[n[1]]
            if n[2] in one.keys():
                rom += one[n[2]]
        if a == 4:
            if n[0] in tho.keys():
                rom += tho[n[0]]
            if n[1] in hun.keys():
                rom += hun[n[1]]
            if n[2] in ten.keys():
                rom += ten[n[2]]
            if n[3] in one.keys():
                rom += one[n[3]]
        return rom