#!/usr/bin/env python3
import sys

lines = []
for line in sys.stdin:
	newline = line.split(":")
	if newline[0] == "\n":
		continue
	newline = list(map(lambda s: s.strip(), newline))
	lines.append(newline)
print(lines, '\n')
for line in lines:
	if line[0][0] == '#':
		print("{} is skipped because it starts with a hashtag (is commented out)".format(line[0]))
	else:
		print("The user {} has a password of {} and has userid {} and groupid {}".format(line[0], line[1], line[2], line[3]))
print("End of User Data")
