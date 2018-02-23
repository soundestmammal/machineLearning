# Compares two numbers to determine if it is 
# Larger or smaller than adjacent number

# Bubble Sort

theList = ['b', 'a', 's', 'e', 'b', 'a', 'l', 'l']

def bubbleSort (myList):
	for i in range (0, len(myList) - 1):
		for j in range(0, len(myList) - 1 - i):
			if myList[j] > myList[j+1]:
				myList[j], myList[j+1] = myList[j+1], myList[j]
	return myList

print(bubbleSort(theList))