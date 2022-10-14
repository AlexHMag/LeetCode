"""Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element
twice.

You can return the answer in any order.

nums = [2,7,11,15]
target = 9
"""

class Solution:
    def twoSum(self, nums, target):
        dic = {}

        for m in range (0, len(nums)):
            temp = target - nums[m]
            if temp in dic:
                return [dic[temp], m]
            else:
                dic[nums[m]] = m
        print(dic)

def main():
    nums = [2,7,11,15]
    target = 9

    test = Solution()
    test.twoSum(nums, target)
    print(test.twoSum(nums, target))

if __name__ == "__main__":
    main()