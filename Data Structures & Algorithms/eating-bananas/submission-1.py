class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        low = 1
        high = piles[-1]
        current = high

        while low <= high:
            k = (low + high) // 2
            curr_h = 0
            
            for p in piles:
                curr_h += math.ceil(p / k)
                print(f"k: {k} curr_h: {curr_h}")

            if curr_h <= h:
                current = k
                high = k - 1
            else:
                low = k + 1
        
        return current