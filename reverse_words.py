#!/usr/bin/env python3
#
# Write a function reverse_words() that takes a message
# as a list of characters and reverses the order of the
# words in place.

def reverse_characters(message):
	left = 0
	right = len(message) - 1
	while left < right:
		temp = message[left]
		message[left] = message[right]
		message[right] = temp
		left += 1
		right -= 1

def reverse_words(message):
	pass

message = ["E", "t", "h", "a", "n",
		   " ", "R", "o", "g", "e",
		   "r", "s"]


# message = [ 'c', 'a', 'k', 'e', ' ',
            # 'p', 'o', 'u', 'n', 'd', ' ',
            # 's', 't', 'e', 'a', 'l' ]

reverse_characters(message)
reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))