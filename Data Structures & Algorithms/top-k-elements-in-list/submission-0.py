class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort(reverse=True)
        top_k_arr = arr[:k]

        result = []
        for i in top_k_arr:
            a = i[1]
            result.append(a)
        return list(result)
