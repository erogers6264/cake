#!/usr/bin/env python3
# Merge meetings

def merge_meetings(meetings):
	# Sort the meetings by start time
	sorted_meetings = sorted(meetings)

	# Add the first meeting to a stack
	merged = [sorted_meetings.pop(0)]

	# Begin iterating through the rest
	for meeting in sorted_meetings:
		# If the last meeting's end time is the same or later than
		# the next meeting's start time, merge them
		if merged[-1][1] >= meeting[0]:
			new_start_time = merged[-1][0]
			new_end_time = meeting[1]
			merged.pop()
			merged.append((new_start_time, new_end_time))
		# Otherwise just add it to the stack unmerged
		else:
			merged.append(meeting)
	return merged

# Should return [(0, 1), (3, 8), (9, 12)]
print(merge_meetings([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
