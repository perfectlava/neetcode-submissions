class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = {}
        end = {}
        max_len = 0

        # start --> 3, 4, 5, 6, 7<--end
        for n in nums:
            if end.get(n-1) == None and start.get(n+1) == None:
                end[n] = end.get(n, n)
                start[n] = start.get(n, n)

            elif end.get(n-1) != None and start.get(n+1) == None:
                end[n] = end[n-1]
                del end[n-1]
                start[end[n]] = n

            elif start.get(n+1) != None and end.get(n-1) == None:
                start[n] = start[n+1]
                del start[n+1]
                end[start[n]] = n
                
            else:
                end_elem = start[n+1]
                start_elem = end[n-1]
                start[start_elem] = end_elem
                end[end_elem] = start_elem
                del start[n+1]
                del end[n-1]
            

        for start, end in start.items():
            max_len = max(max_len, end - start + 1)


        return max_len