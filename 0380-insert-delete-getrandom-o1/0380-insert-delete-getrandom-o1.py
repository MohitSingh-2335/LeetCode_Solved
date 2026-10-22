import random
class RandomizedSet:
    def __init__(self):
        self.l=[]
        self.d={}
    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.l.append(val)
            self.d[val] = len(self.l)-1
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        if val in self.d:
            temp=self.d[val]
            temp2=self.l[-1]
            self.l[temp] = temp2
            self.d[temp2] = temp
            self.l.pop()
            del self.d[val]
            return True
        else:
            return False
    def getRandom(self) -> int:
        a = random.choice(self.l)
        return a
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()