class Solution:
    def numOfWays(self, n: int) -> int:
        aba = 6
        abc = 6
        for _ in range(n - 1):
            aba, abc = 3 * aba + 2 * abc, 2 * aba + 2 * abc
        return (aba + abc) % (10**9 + 7)



print(Solution().numOfWays(10))