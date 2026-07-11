class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {}
        count = len(position)        

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars[position[i]] = time
        
        position.sort(reverse=True)

        for i in range(1, len(position)):
            if cars[position[i-1]] >= cars[position[i]]:
                cars[position[i]] = cars[position[i-1]]
                count -= 1

        return count
