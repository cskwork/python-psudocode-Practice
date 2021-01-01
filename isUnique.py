"""
Question
You are given a string. Write a function to determine if all of the characters in the string appear only once.

Your function shouldn't care about capitalization. A is the same as a.

1Input - "heLlo"
2Output - False
3
4Input - "hey"
5Output - True
6
"""
#Brute
def isUnique(s):
	s= s.lower()
	# c is counter, L is letter
	for c1,l1 in enumerate(s):
		for c2,l2 in enumerate(s):
			if c1 == c2:
				continue
			if l1 == l2:
				return False
	return True

#Opt
def isUnique2(s):
	s=s.lower()
	seen=set()
	for c in s:
		if c in seen:
			return False
		else:
			seen.add(c)
	return True

#Follow
def isUnique3(s):
	s=sorted(s.lower())
	for i in range(1, len(s)):
		if s[i] == s[i-1]:
			return False
	return True

print(isUnique3('hello'))
print(isUnique3('hey'))


