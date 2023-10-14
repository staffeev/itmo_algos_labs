class Solution:
    # https://leetcode.com/problems/advantage-shuffle/description/
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        nums1 = sorted(nums1)
        p1, p2 = 0, n - 1
        positions = sorted(range(n), key=lambda x: nums2[x], reverse=True)
        for pos in positions:
            if nums1[p2] > nums2[pos]:
                nums2[pos] = nums1[p2]
                p2 -= 1
            else:
                nums2[pos] = nums1[p1]
                p1 += 1
        return nums2