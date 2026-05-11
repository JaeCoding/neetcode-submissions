class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        topK = count.most_common(k)
        return [num for num, _ in topK]