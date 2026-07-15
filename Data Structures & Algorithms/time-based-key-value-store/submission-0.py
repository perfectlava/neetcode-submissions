class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value]
)
    def get(self, key: str, timestamp: int) -> str:
        tar_list = self.data[key]
        r = len(tar_list) - 1
        l = 0 
        newest = [-1, ""]


        while l <= r:
            mid = (l + r) // 2
            if tar_list[mid][0] <= timestamp:
                l = mid + 1
                newest = tar_list[mid]
            else:
                r = mid - 1
        
        return newest[1]


        
