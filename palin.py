#!/usr/bin/python
name = "racecar"
print "{0:<20s}{1}".format("Word:",name);
name2 = name[::-1]
print "{0:<20s}{1}".format("reverse:" name2);
if name==name2:
	print "Yes Palindrome"
else:
	print"not palindrome"
