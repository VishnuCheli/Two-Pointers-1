#Time Complexity:: O(m+n)- traversing all elements in nums1 and nums2 
#Space Complexity:: O(1)-no extra space used
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        first = m-1 #length of num1 array, pointer is in nums1
        second = n-1 #length of num2 array, pointer is in nums2
        third = m+n - 1 
        
        while first>=0 and second>=0: #assurring that 1st and 2nd pointers start at end of the lists
            if nums1[first] < nums2[second]: #if the nums2 value is larger than its copied to nums1
                nums1[third] = nums2[second]
                second -= 1 #pointer of nums2 is shifted to left
            else: #if nums1 has same values then nums1 pointer shifted till first pointer goes out of bound
                nums1[third] = nums1[first]
                first -= 1
            third -= 1 #no matter wate the third pointer keeps moving to the left
            
        if second >= 0: #all the nums2 values copied to nums1 if second pointer still hasn't gone out of bound
            nums1[:second+1] = nums2[:second+1]
        
        