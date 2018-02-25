def linearSearch(myList, item):
	for i in range(0, len(myList)):
		if myList[i] == item:
			return print(item + "was found at position " + i)
	return print("-1. Search Unsuccessful");	