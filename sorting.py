def insertionSort(alist):
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index

		while position>0 and alist[position-1]>currentvalue:
			alist[position]=alist[position-1]
			position = position-1

		alist[position]=currentvalue




if __name__ == '__main__':
	# UnsortedList = input("Give an unsorted list: ")
	ListToSort = [3,2,4,5,1]
	insertionSort(ListToSort)
	print(ListToSort)
