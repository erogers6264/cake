#!/usr/bin/env python3

# Keep track of the first and last indices of characters

# Find the first and last characters and swap them

# Increment the first index and decrement the last

# Swap those characters

# Keep going until you've reached the middle

# If the character count is even, then you can stop when second index minus first index is one

# If the character count is odd, then stop when second index minus first index is two


def swap(first_index, second_index, list_of_chars):
	temp = list_of_chars[first_index]
	list_of_chars[first_index] = list_of_chars[second_index]
	list_of_chars[second_index] = temp


def reverse_in_place(list_of_chars):
	first_index = 0
	second_index = len(list_of_chars) - 1
	char_count = len(list_of_chars)

	while True:
		swap(first_index, second_index, list_of_chars)

		if char_count % 2 == 0 and second_index - first_index == 1:
			break
		if char_count % 2 == 1 and second_index - first_index == 2:
			break

		first_index += 1
		second_index -= 1



example = ["a", "b", "c", "d", "e"]
print(example)
reverse_in_place(example)
print(example)

