import string

def verify(isbn):
	nums = []
	
	for x in isbn:
		if x in string.digits or (x == "X") and x in isbn[-2:]:
			nums += x
			
	nums = [x.replace("X", "10") for x in nums]
	nums = [int(x) for x in nums]
	numslen = list(range(len(nums),0,-1))
	result = [a*b for a,b in zip(nums,numslen)]

	if len(nums) != 10:	
		return False
		
	if sum(result) % 11 == 0:
		return True
	
	else:
		return False
	
	
