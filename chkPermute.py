"""
The input is two strings. Check if the first string is a permutation of the second string.

1Input - "wazup bro", " orbpuwaz"
2Output - True
3
4Input - "hiiiya", "hiya"
5Output - False
6

1. Restate Question in own words. Determine input, output, label, condition
Check if 1 string is permutation of 2 string (all letters of it contained)
input 2 string
def chkPerm(str1,str2)
output t/f
2. Make Simple Test Case
"waz", " azw"
true
3. Write/Draw Pseudocode
make map of str1
cnt +1 if char exist
check if str2 has same cnt of char map as str1
return t/f
4. Analyze/Compare to answer if false write fixed pseudocode
make dict of str1
cnt ++1 if char exist, if not in dict set to 1
check str2 to str1 dict and if char is in dict --1. if not return false
return t if dict is 0
5. Write code answer
"""
#Brute
def chkPerm(s1,s2):
	s1, s2 = sorted(s1), sorted(s2)
	return s1 == s2
#Opt
def chkPerm2(s1,s2):
	count = {}
	for i in s1:
		if i in count:
			count[i] +=1
		else:
			count[i] = 1
	for i in s2:
		if i in count:
			count[i] -=1
		else:
			return False
		if count[i] == 0:
			del count[i]
	return True

#Follow(option)

print(chkPerm2('hello','lloeh')) #True
print(chkPerm2('hey','heeyy')) #False