class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) * len(matrix[0]) - 1 

        while low <= high:
            mid = (high + low) // 2

            val = matrix[mid // len(matrix[0])][mid % len(matrix[0])]

            if val < target:
                low = mid + 1 
            elif val > target:
                high = mid - 1
            else:
                return True
        
        return False
