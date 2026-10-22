class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        sta = 0
        c_tank = 0
        t_tank = 0
        if sum(gas) < sum(cost):
            return -1
        else:
            for k in range(len(gas)):
                tank = gas[k] - cost[k]
                c_tank += tank
                if c_tank < 0:
                    c_tank = 0
                    sta = k+1
        return sta