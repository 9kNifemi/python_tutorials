#!/usr/bin/env python3
#Longest consecutive sequence leetcode hard by Nifemi Olafisan
'''
Let's solve another classic LeetCode hard problem: "Longest Consecutive Sequence". This problem focuses on finding the length of the longest consecutive elements sequence in an unsorted array. It's a great problem for understanding hash sets and efficient lookups.

Problem Statement: Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example:
	
Input: nums = [100, 4, 200, 1, 3, 2]

Output: 4

Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Strategy:
	
Use a Hash Set: First, convert the array into a set to allow for O(1) lookups, removing duplicates in the process.
Iterate Over the Array: Go through each number in the array. For each number, check if it's the start of a sequence by seeing if num - 1 is not in the set.
Expand the Sequence: If it's the start of a sequence, iteratively check for the next numbers in the sequence (num + 1, num + 2, ...) and count how long the sequence is.
Track the Maximum: Keep track of the maximum length of any sequence found.
Python Implementation:
	
Let's implement this approach in Python and ensure it outputs the result.
The solution to the "Longest Consecutive Sequence" problem has been successfully implemented and executed. Given the input array nums = [100, 4, 200, 1, 3, 2], the output is 4. This indicates that the longest consecutive elements sequence in the array is [1, 2, 3, 4], and therefore, its length is 4.

Here's a brief overview of how the solution works:
'''
def longest_consecutive(nums):
	if not nums:
		return 0
	
	nums_set = set(nums)  # Convert list to set for O(1) lookups
	max_length = 0
	
	for num in nums_set:
		# Check if num is the start of a sequence
		if num - 1 not in nums_set:
			current_num = num
			current_length = 1
			
			# Expand the sequence as long as consecutive numbers are found
			while current_num + 1 in nums_set:
				current_num += 1
				current_length += 1
				
			max_length = max(max_length, current_length)  # Update max_length if current sequence is longer
			
	return max_length

# Example usage
nums = [100, 4, 200, 1, 3, 2]
output = longest_consecutive(nums)
print(output)  # Prints the length of the longest consecutive sequence

'''
This approach ensures that the algorithm runs in O(n) time complexity, as it iterates through the set of numbers only once and uses set operations that have an average time complexity of O(1) for checking the presence of elements. This solution efficiently finds the longest consecutive sequence without needing to sort the array, demonstrating an effective use of hash sets for performance optimization in Python.'''