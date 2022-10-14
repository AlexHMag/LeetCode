"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of 
the two sorted arrays.

The overall run time complexity should be O(log (m+n))."""

class Solution(object):
    def findMedianSortedArray(self, nums1, nums2):
        nums1 += nums2
        nums1.sort()

        if len(nums1) % 2 == 0:
            aux = (len(nums1) - 1) // 2
            return (nums1[aux] + nums1[aux + 1]) / 2
        else:
            aux = len(nums1) // 2
            return nums1[aux]

def main():
    nums1 = [1,2]
    nums2 = [3,4]

    test = Solution()
    test.findMedianSortedArray(nums1, nums2)
    print(test.findMedianSortedArray(nums1, nums2))

if __name__ == "__main__":
    main()