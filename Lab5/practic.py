class Solution:
    # https://leetcode.com/problems/trapping-rain-water/
    def trap(self, height: list[int]) -> int:
        n = len(height)
        left_ix = 0
        right_ix = n - 1
        left_max = right_max = 0
        s = 0
        while left_ix <= right_ix:
            if height[left_ix] <= height[right_ix]:
                left_max = max(left_max, height[left_ix])
                s += left_max - height[left_ix]
                left_ix += 1
            else:
                right_max = max(right_max, height[right_ix])
                s += right_max - height[right_ix]
                right_ix -= 1
                
        return s


if __name__ == "__main__":
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap(height))