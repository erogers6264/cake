#!/usr/bin/env python3
# Merge meetings

def is_mergeable(meeting1, meeting2):
	# Sort the two meetings by start time
	meetings = sorted([meeting1, meeting2])

	# If the end time of the first meeting is later than or the same as the
	# start time of the second meeting then they are mergeable:
	if meetings[0][1] >= meetings[1][0]:
		return True
	else:
		return False


print("The meetings are mergeable: " + str(is_mergeable((2, 7), (4, 10))))
