#!/usr/bin/env python3

#Python List Tutorial by Nifemi Olafisan

#1. Creating lists and accessing elements
# The following snippet demonstrates how to create a list, access its elements, and use basic indexing.
# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Accessing elements
print("First element:", fruits[0])
print("Second element:", fruits[1])

# Negative indexing (accessing from the end)
print("Last element:", fruits[-1])

#2. Modifying lists
#The following snippet demonstrates how to add, remove, and modify elements in a list.
# Modifying an element
fruits[1] = "blueberry"
print("Modified list:", fruits)

# Appending an element
fruits.append("orange")
print("After appending:", fruits)

# Inserting an element at a specific position
fruits.insert(1, "banana")
print("After inserting:", fruits)

# Removing an element
fruits.remove("apple")
print("After removing:", fruits)

# Removing the last element
popped_fruit = fruits.pop()
print("Popped fruit:", popped_fruit)
print("List after popping:", fruits)

#3. List operations and functions
#The following snippet demonstrates slicing, concatenation, and finding the length of a list, along with some useful list functions.
# Slicing lists
print("First two elements:", fruits[0:2])
print("Elements from second to last:", fruits[1:])

# Concatenating lists
vegetables = ["carrot", "potato", "cucumber"]
print("Concatenated list:", fruits + vegetables)

# Finding the length of a list
print("Number of fruits:", len(fruits))

# Useful functions
print("Maximum (alphabetically):", max(fruits))
print("Minimum (alphabetically):", min(fruits))
print("Count of 'banana':", fruits.count("banana"))


#4. Iterating Over Lists
#The following snippet demonstrates how to loop through a list using for loops and list comprehensions.
# Using a for loop
for fruit in fruits:
	print("Fruit:", fruit)
	
# List comprehension (creating a new list with modified elements)
uppercase_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", uppercase_fruits)


#5. Sorting and Reversing Lists
#The following snippet demonstrates how to sort lists both in ascending and descending order, and how to reverse them.
# Sorting a list
fruits.sort()
print("Sorted list:", fruits)

# Sorting in descending order
fruits.sort(reverse=True)
print("Sorted list in descending order:", fruits)

# Reversing a list
fruits.reverse()
print("Reversed list:", fruits)


#Problem : Merge Intervals
'''
Given an array intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]

Output: [[1,6],[8,10],[15,18]]

Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
'''
'''
Strategy:
1.Sort the intervals: First, we sort the intervals based on the starting times. 
  This makes it easier to find overlapping intervals.
2.Merge Overlapping Intervals: Iterate through the sorted intervals, and for each interval, if it overlaps with the previous one 
  (i.e., its start time is less than or equal to the end time of the previous interval), we merge them. Otherwise, 
  we add the current interval to the output list as it does not overlap with any previous intervals.

'''
'''
Function Definition: merge_intervals(intervals) is defined to process a list of intervals.

Sorting: intervals.sort(key=lambda x: x[0]) sorts the intervals based on their start time. 
This is crucial for simplifying the merging process, as it ensures that any potential overlaps are consecutive in the list.

Initialize the Merged List: merged = [intervals[0]] starts the merged list with the first interval, assuming the list is not empty.

Iterate Through Intervals: The script iterates through the sorted intervals starting from the second element.

Merge Overlapping Intervals: Within the loop, it checks if the current interval overlaps with the last interval in the merged list. 
Overlapping is determined by comparing the start of the current interval with the end of the last merged interval. 
If they overlap, the end of the last merged interval is updated to the maximum of its own end and the end of the current interval.

Append Non-Overlapping Intervals: If the current interval does not overlap with the last one in the merged list, 
it's added to merged as a new, separate interval.

Return Merged Intervals: Finally, the function returns the merged list containing all the merged intervals.
'''
#solution:
def merge_intervals(intervals):
	# Sort the intervals based on the start time
	intervals.sort(key=lambda x: x[0])
	
	# Initialize the merged list with the first interval
	merged = [intervals[0]]
	
	for current in intervals[1:]:
		# If the current interval overlaps with the last interval in merged, merge them
		if current[0] <= merged[-1][1]:
			merged[-1][1] = max(merged[-1][1], current[1])
		else:
			# If they don't overlap, add the current interval to merged
			merged.append(current)
			
	return merged

# Test the function with the example input
intervals = [[1,3],[2,6],[8,10],[15,18]]
output = merge_intervals(intervals)
print(output)
