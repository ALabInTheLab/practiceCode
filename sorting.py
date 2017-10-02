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
def mergeSort3(alist):
	# print("Splitting ",alist)
	if len(alist) > 1:
		onethird = len(alist)//3
		print(onethird)
		left = alist[0:onethird]
		mid = alist[onethird:onethird*2]
		right = alist[onethird*2:len(alist)]
		# print(left,'\n',right)

		mergeSort(left)
		mergeSort(mid)
		mergeSort(right)

		l, m, r, k= 0, 0, 0, 0
		while l < len(left) and m < len(mid) and r < len(right):
			if left[l] < min(mid[m], right[r]):
				alist[k] = left[l]
				l = l+1
			elif right[r] < min(mid[m], left[l]):
				alist[k] = right[r]
				r = r+1
			else:
				alist[k] = mid[m]
				m = m+1
			k = k+1
		
		while r < len(right):
			alist[k] = right[r]
			r = r +1
			k = k+1

		while m < len(mid):
			alist[k] = mid[m]
			m = m+1
			k = k+1

		while l < len(left):
			alist[k] = left[l]
			l = l+1
			k = k+1
	# print("Merging", alist)

def quickSort_init(alist):
	low = 0
	high = len(alist) - 1
	quickSort(alist, low, high)


def quickSort(alist, low, high):
	if low < high:
		border = partition(alist, low, high)
		quickSort(alist, low, border-1)
		quickSort(alist, border+1, high)

def partition(alist, low, high):
	pivot = alist[high]
	i = low-1

	for j in range(low,high):
		print("j= ",j)
		if alist[j] <= pivot:
			i = i +1
			print("i = ",i)
			alist[j], alist[i] = alist[i], alist[j]
			print(alist)

	alist[i+1], alist[high] = alist[high], alist[i+1]
	return i+1
	print(alist)




	


if __name__ == '__main__':
	# UnalistList = input("Give an unalist list: ")
	alist = [8,9,7,2,5,4,1,3,6,4] #,14,32,6,9,24,82
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

	mergeSort3(alist)
	print("Merge Sort (split N/3)",
		"\nLength: ", listLen,
		"\nSorted List: ", alist)

	# quickSort_init(alist)
	# print("\nSorted List: ", alist)


