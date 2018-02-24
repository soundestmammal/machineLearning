# Try and find the smallest item
# Put it in the first position [0]
# Everything to right will still be unsorted

A = [8, 3, 2, 5, 4, 7, 9]

def sel(A):
	for i in range (0, len(A) - 1):
		minIndex = i
		for j in range (i+1, len(A)):
			if A[j] < A[minIndex]:
				minIndex = j
		if minIndex != i:
			A[i], A[minIndex] = A[minIndex], A[i]