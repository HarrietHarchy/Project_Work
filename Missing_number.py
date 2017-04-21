#find the missing number in an array
def findMissing(numArray,maxNum):
	input=[1,2,3,5,6,7,8,9,10]
	toReturn =4
	for i in range(1,10):
		numArray =[1]
		found=False

	while(i<=maxNum and not found):
		i+=1
		if not numArray:
			found =True
			return toReturn
		else:
			return toReturn

print findMissing(0,10)