#Time Complexity:: O(n)-comparing hieghts from left and right
#Space Complexity:: O(1)-no extra space used
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low = 0
        high = len(height)-1
        
        max_area = 0 #keeps track of max area calculated so far
        
        while low < high: #compare current max and next max height, min of the next low-height and high-height defines max_area
            max_area = max(max_area,(min(height[low],height[high])*(high-low)))
            
            if height[low] < height[high]: #move the low or high pinter towards the direction with lower height
                low += 1
            else:
                high -= 1
                
        return max_area