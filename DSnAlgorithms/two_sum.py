#Eugenio Ramirez
#05/08/2024
#Two Sum Problem [https://leetcode.com/problems/two-sum/description/]

"""
    Given an array of integers "nums" and an integer "target", return indices of the two numbers such that they add up to "target"
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order

    Example:

    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: Because nums[0] + nums[1] == 0, we can return [0, 1]
"""
import copy
class Solution:
    def twoSums(self, nums: list[int], target: int ) -> list[int]:
        #To store index of sum
        indx = []

        #If we don't use this, the list is going to be copy by reference
        cp = copy.deepcopy(nums)

        #These are two pointers for binary search. They point to the minimum and maximum value of the given numbers
        low = cp.pop(cp.index(min(cp)))
        high = cp.pop(cp.index(max(cp)))


        #Binary search algorithm variation
        while low <= high:

            if low + high < target:
                low = cp.pop(cp.index(min(cp)))

            elif low + high > target:
                high = cp.pop(cp.index(max(cp)))

            else:
                break
            
        #The list.index(value) function returns the index of the first occurrence of the given value if found multiple times.
        if low == high:
            indx.append(nums.index(low))
            nums.pop(nums.index(low))
            indx.append(nums.index(high) + 1)

        print(indx)

if __name__ == '__main__':
    #Put here the array you want to test
    nums = [3, 3]

    #Put here the desired target
    target = 6

    s = Solution()
    s.twoSums(nums=nums, target=target)

        


            
