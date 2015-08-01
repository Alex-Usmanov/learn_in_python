# coding:utf-8
'''
https://leetcode.com/problems/two-sum/
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

Show Tags
Show Similar Problems

'''


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    pass


def twoSum(nums, target):
    # index1=1
    # index2=2
    for i in range(len(nums)):
        num1 = nums[i]
        index1 = i + 1
        for j in range(i, len(nums) - i):
            num2 = nums[j]
            index2 = j + 1
            if target == num1 + num2:
                return index1, index2
    return None


def twoSum2(nums, target):
    for i in range(len(nums)):
        num1 = nums[i]
        index1 = i + 1
        num2 = target - num1
        if num2 in nums:
            index2 = nums.index(num2) + 1
            return index1, index2
    return None


def test1():
    nums = [2, 7, 11, 15]
    # s=Solution
    print twoSum(nums, target=9)
    print twoSum2(nums, 9)
    print twoSum2(nums, 18)


def test2():
    nums = [1, 9, 3, 20, 45]
    print twoSum(nums, 29)
    print twoSum2(nums, 4)
    print twoSum2(nums, 54)


if __name__ == "__main__":
    test1()
    test2()
