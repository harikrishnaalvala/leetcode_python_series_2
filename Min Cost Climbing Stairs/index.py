class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lenght = len(cost) + 1
        answer = [0] * lenght
        for i in range(2, lenght):
            answer[i] = min(answer[i - 1] + cost[i - 1], answer[i - 2] + cost[i - 2])
        return answer[lenght - 1]
