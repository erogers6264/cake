#!/usr/bin/env python3
# Merge meetings

def merge_meetings(meetings):
	sorted_meetings = sorted(meetings)
	merged = [sorted_meetings.pop(0)]
	for meeting in sorted_meetings:
		if merged[-1][1] >= meeting[0]:
			new_start_time = merged[-1][0]
			new_end_time = meeting[1]
			merged.pop()
			merged.append((new_start_time, new_end_time))
		else:
			merged.append(meeting)
	return merged

# Should return [(0, 1), (3, 8), (9, 12)]
print(merge_meetings([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
