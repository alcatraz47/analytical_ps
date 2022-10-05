def two_pointers(arr: list, k: int):
	i = 0
	j = len(arr) - 1
	while (i < j):
		if arr[i] + arr[j] > k:
			j -= 1
		elif arr[i] + arr[j] < k:
			i += 1
		elif arr[i] + arr[j] == k:
			return True
		return False

if __name__=="__main__":
	arr = [2, 3, 4, 5]
	arr = arr.sort()
	k = 9
	print(two_pointers(arr, k))
