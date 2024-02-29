#!/usr/bin/env python3
#Trapping rainwater problem by Nifemni Olafisan
'''
Problem Statement: Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example:
	
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output: 6

Explanation: The above elevation map (represented by the array [0,1,0,2,1,0,1,3,2,1,2,1]) is depicted in a visual format, 
showing that a total of 6 units of rainwater (blue section) are being trapped.

Strategy:
	
Two Pointer Approach: Use two pointers, left and right, starting at the beginning and end of the array, respectively. 
Maintain two variables, left_max and right_max, to keep track of the maximum height seen so far from the left and right.
Traverse the Height Array: Move the left and right pointers towards each other. At each step:
Update left_max and right_max based on the current heights.
If left_max is less than right_max, water trapped on the current left position is 
left_max - height[left] (since the water level is determined by the lower of the two maxes), and move left to the right.
If right_max is less or equal to left_max, do the analogous operation for right and move right to the left.
Calculate Water Trapped: Keep adding the water trapped at each step to a total sum.
Python Implementation:
	
Now, let's implement this solution in Python.
The solution to the "Trapping Rain Water" problem has been successfully implemented. 
Given the input height = [0,1,0,2,1,0,1,3,2,1,2,1], the output is 6. 
This indicates that a total of 6 units of rainwater can be trapped after raining, 
considering the elevation map represented by the array.

Here's a quick rundown of the solution: '''
def trap(height):
	left, right = 0, len(height) - 1
	left_max, right_max = 0, 0
	trapped_water = 0
	
	while left < right:
		if height[left] < height[right]:
			if height[left] >= left_max:
				left_max = height[left]
			else:
				trapped_water += left_max - height[left]
			left += 1
		else:
			if height[right] >= right_max:
				right_max = height[right]
			else:
				trapped_water += right_max - height[right]
			right -= 1
			
	return trapped_water

# Test the function with the example input
height = [0,1,0,2,1,0,1,3,2,1,2,1]
output = trap(height)
print(output)  # Make sure to include this line to print the output

'''
The script employs a two-pointer approach to efficiently calculate the amount of trapped water. 
It iterates over the array only once, maintaining two pointers from both ends of the array and moving inward. 
By keeping track of the maximum heights encountered from both sides (left_max and right_max), 
it calculates the trapped water at each step by finding the difference between the current height and the maximum height encountered so far from the corresponding side.'''