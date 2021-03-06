from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.search([2,5,6,0,0,1,2], 3) == False