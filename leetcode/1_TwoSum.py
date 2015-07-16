# coding:utf-8

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    pass

def twoSum(nums, target):
        # index1=1
        # index2=2
    for i in range(len(nums)):
        num1=nums[i]
        index1=i+1
        for j in range(i,len(nums)-i):
            num2=nums[j]
            index2=j+1
            if target==num1+num2:
                return index1,index2
    return "sorry,no solution find... "

def test1():
    nums=[2,7,11,15]
    # s=Solution
    print twoSum(nums,target=9)

def test2():
    nums=[1,9,3,20,45]
    print twoSum(nums,29)

if __name__=="__main__":
    test1()
    test2()
