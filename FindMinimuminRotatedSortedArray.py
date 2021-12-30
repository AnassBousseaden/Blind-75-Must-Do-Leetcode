class Solution:
    def findMin(self, nums: list[int]):
        left, right = 0, len(nums)-1
        mid = ((right + left) // 2)
        m = nums[0]
        while left < right:
            print(left, mid, right)
            if nums[left] < nums[right]:
                return min(nums[left], m)
            # nums[left]>nums[right]
            if nums[mid] <= nums[right]:
                m = min(nums[mid], m)
                right = mid - 1
            else:  # nums[mid]>nums[right]
                m = min(nums[mid], m)
                left = mid + 1
            mid = ((right + left) // 2)
        print(m)
        return min(nums[mid], nums[left], nums[right], m)


test = Solution()

t = [4, 5, 1, 2, 3]

print(test.findMin(t))
