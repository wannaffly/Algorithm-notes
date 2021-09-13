#动态规划

class Solution:
    # 70. 爬楼梯
    # 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    # 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    def climbStairs(self, n: int) -> int:
        dp = [0,1,2]
        for i in range(3,n+1):
            dp.append(dp[i-1]+ dp[i-2])
        return dp[n]


    def maxProfit(self, prices):
        pro = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                pro.append(prices[j]-prices[i])
        pro = sorted(pro)
        return pro.pop() if pro.pop() > 0 else 0

    # def maxProfit(self, prices):
    #     minprice = prices[0]
    #     maxprofit = 0
    #     for i in range(1,len(prices)):
    #         profit = prices[i] - minprice
    #         if profit > maxprofit:
    #             maxprofit = profit
    #         if prices[i] < minprice:
    #             minprice = prices[i]
    #     return maxprofit
    
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for i in range(m)]

        maxsquare = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    if i-1 != 0 and j-1 != 0:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                maxsquare = max(maxsquare,dp[i][j])
        return maxsquare**2

    def coinChange(self, coins, amount):
        mincoins = [float('inf') for i in range(amount+1)]
        mincoins[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i-coin >= 0:
                    mincoins[i] = min(mincoins[i], mincoins[i - coin] + 1)
        return mincoins[amount] if mincoins[amount] != float('inf') else -1

    def maxSubArray(self, nums):
        n = len(nums)
        dp = [nums[0] for i in range(n)] 
        for i in range(n):
            for j in range(i+1):
                dp[i] = max(dp[i],dp[i-1],sum(nums[j:i+1]))
        return dp[n-1]

s = Solution()
matrix = [1,2,-4,5]
s.maxSubArray(matrix)
