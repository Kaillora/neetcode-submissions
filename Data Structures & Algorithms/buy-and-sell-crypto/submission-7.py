class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize the left and right pointers of the array, and the best profit we can acheive
        l, r = 0, 1
        best = 0

        # if l < r, then right pointer - left pointer and take best profit. if l > r, move left pointer
        # to right pointer position and increment right pointer by 1.
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                best = max(best, profit)
            else:
                l = r
            r += 1
        return best