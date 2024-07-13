class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        n = len(nums)
        max_avg = float("-inf")
        cur_avg = sum(nums[:k])
        max_avg = cur_avg / k
        

        while i + k + 1 <= n:
            cur_avg -= nums[i]
            cur_avg += nums[i+k]

            if max_avg < cur_avg / k:
                max_avg = cur_avg / k

            i += 1
        return max_avg
