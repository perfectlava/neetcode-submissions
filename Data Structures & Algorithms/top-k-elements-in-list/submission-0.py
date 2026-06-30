class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        for i in range(k):
            max_key = max(freq, key=freq.get)
            del freq[max_key]
            out.append(max_key)
        
        return out