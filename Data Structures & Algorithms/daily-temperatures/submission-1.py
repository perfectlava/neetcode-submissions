class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        out = [0] * len(temperatures)
        i = t = math.inf
        
        for index, temp in enumerate(temperatures):

            while len(temps) > 0:
                i, t = temps[-1]
                if t < temp:
                    out[i] = index - i
                    temps.pop()
                else:
                    break
            
            temps.append((index, temp))
            print(temps)
        
        
        return out