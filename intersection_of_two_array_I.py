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

def intersect_hash_based(nums1, nums2):
    output = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                if nums1[i] not in output:
                    output.append(nums1[i])
    return output

def intersect_while_loop(nums1, nums2):
    # output
    output = []
    # first take O(nlogn) to sort the two input lists
    nums1.sort()
    nums2.sort()
    # pointer to the current index of the first list
    nums1Pointer = 0
    while nums1Pointer < len(nums1):
        # should have used a while loop
        # avoid unnecessary iterations
        while nums1Pointer + 1 < len(nums1) and nums1[nums1Pointer] == nums1[nums1Pointer + 1]:
            nums1Pointer += 1
        # flag to avoid incorrect increment of pointers
        shouldIncrement = True
        # pointer to the current index of the second list
        nums2Pointer = 0
        while nums2Pointer < len(nums2):
            # avoid unnecessary iterations
            while nums2Pointer + 1 < len(nums2) and nums2[nums2Pointer] == nums2[nums2Pointer + 1]:
                nums2Pointer += 1
            # found intersections
            if nums2[nums2Pointer] == nums1[nums1Pointer]:
                output.append(nums2[nums2Pointer])
                nums1Pointer += 1
                shouldIncrement = False
                break
            nums2Pointer += 1
        if shouldIncrement:
            nums1Pointer += 1
    return output

def intersect_set_optimised(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return set1 & set2



# l1 = [4,9,5]
# l2 = [9,4,9,8,4]

# l1 = [43,85,49,2,83,2,39,99,15,70,39,27,71,3,88,5,19,5,68,34,7,41,84,2,13,85,12,54,7,9,13,19,92]
# l2 = [10,8,53,63,58,83,26,10,58,3,61,56,55,38,81,29,69,55,86,23,91,44,9,98,41,48,41,16,42,72,6,4,2,81,42,84,4,13]

