import math 

def insertionSort(alist):
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index

		while position>0 and alist[position-1]>currentvalue:
			alist[position]=alist[position-1]
			position = position-1

		alist[position]=currentvalue


def sortFraction(left, right):
	i, j, k ,alist= 0, 0, 0, []
	# while (i < len(left)) and (j < len(right)):
	while (k < (len(left) + len(right))):
		if i == len(left):
			while j < len(right):
				alist.append(right[j])
				j = j +1
			k = k+1

		elif j == len(right):
			while i < len(left):
				alist.append(left[i])
				i = i+1
			k = k+1

		else:
			if left[i] < right[j]:
				alist.append(left[i])
				# alist[k] = left[i]
				i = i+1
			else:
				alist.append(right[j])
				# alist[k] = right[j]
				j = j+1
			k = k+1
	else:
		print("This part is done: ", alist)

def MYmergeSort(alist):
	if len(alist) > 1:
		left = alist[0:math.floor(len(alist)/2)]
		right = alist[math.floor(len(alist)/2):len(alist)]
		print(left,'\n',right)

	while len(left) > 1:
		right = left[math.floor(len(left)/2):len(left)]
		left = left[0:math.floor(len(left)/2)]
		print(left,'\n',right)

	i, j, k ,alist= 0, 0, 0, []
	while (k < (len(left) + len(right))):
		if i == len(left):
			while j < len(right):
				alist.append(right[j])
				j = j +1
			k = k+1

		elif j == len(right):
			while i < len(left):
				alist.append(left[i])
				i = i+1
			k = k+1

		else:
			if left[i] < right[j]:
				alist.append(left[i])
				# alist[k] = left[i]
				i = i+1
			else:
				alist.append(right[j])
				# alist[k] = right[j]
				j = j+1
			k = k+1
	else:
		print("This part is done: ", alist)


def mergeSort(alist):
	# print("Splitting ",alist)
	if len(alist) > 1:
		mid = len(alist)//2
		print(mid)
		left = alist[0:math.floor(len(alist)/2)]
		right = alist[math.floor(len(alist)/2):len(alist)]
		# print(left,'\n',right)

		mergeSort(left)
		mergeSort(right)

		i, j, k= 0, 0, 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				alist[k] = left[i]
				i = i+1
			else:
				alist[k] = right[j]
				j = j+1
			k = k+1
		
		while j < len(right):
			alist[k] = right[j]
			j = j +1
			k = k+1

		while i < len(left):
			alist[k] = left[i]
			i = i+1
			k = k+1
	# print("Merging", alist)

def partition(alist, l, r):
	# l = 0
	# high = len(alist)-1
	# print(high)
	pivot = alist[r]
	i = l-1

	for j in range(l,r):
		# print("j= ",j)
		if alist[j] <= pivot:
			i = i +1
			# print("i = ",i)
			alist[j], alist[i] = alist[i], alist[j]
		# print(alist)

	alist[i+1], alist[r] = alist[r], alist[i+1]
	return i+1
	# print(alist)

def quickSort(alist, p, q):
	if p < q:
		m = partition(alist, 0, len(alist)-1)
		quickSort(alist, p, m-1)
		quickSort(alist, m+1, q)
	


if __name__ == '__main__':
	# UnalistList = input("Give an unalist list: ")
	alist = [10, 80, 30, 90, 40, 50, 70] #,14,32,6,9,24,82
	listLen = len(alist)
	print("\nInitial List: ", alist)

	# insertionSort(alist)
	# print("Insertion Sort",
	# 	"\nLength: ",listLen,
	# 	"\nSorted List: ", alist)

	# mergeSort(alist)
	# print("Merge Sort",
	# 	"\nLength: ", listLen,
	# 	"\nSorted List: ", alist)

	quickSort(alist, 0, len(alist)-1)
	print("\nSorted List: ", alist)


