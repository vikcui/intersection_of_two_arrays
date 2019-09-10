# author: YANG CUI
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""

from collections import Counter
def intersect_collections_counter(nums1, nums2):
    """
    :param nums1: input list 1
    :param nums2: input list 2
    :return: the intersection of the two lists
    :time complexity: O(t) t being total number of elments in two lists combined
    """
    # find the intersection between two sets (every element appears once)
    intersection_set = set(nums1) & set(nums2)
    # construct Counter hashables
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)
    # output
    output = []
    for element in intersection_set:
        # find the number of times a duplicate should appear in the result or any at all, if not min will be 0
        lowest_occurance = min(counter1[element], counter2[element])
        for time in range(lowest_occurance):
            output.append(element)
    return output