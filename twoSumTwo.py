#167. Two Sum II - Input Array Is Sorted

class Solution(object):
    def twoSumTwo(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = 0
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            res = numbers[l] + numbers[r]
            if res > target:
                r -= 1
            elif res < target:
                l += 1
            else:
                return [l + 1, r + 1]

        return []

# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [2,7,11,15]
    target = 9
    print("Output is:", sol.twoSumTwo(nums, target))
