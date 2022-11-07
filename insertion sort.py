# Insertion sort
def insertion_sort_for(array: list[int]) -> list[int]:
	for i in range(1, len(array)):
		key = arr[i]
		j = i-1
		while j >= 0 and key < array[j]:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = key
	return array


def insertion_sort_while(array: list[int]):
	i, m = 1, 0
	while i < len(array):
		m = i - 1
		while m >= 0:
			if array[m] > array[i]:
				array[m], array[i] = array[i], array[m]
				i -= 1
			m -= 1
		i += 1
	return array


arr = [12, 11, 13, 5, 6]
print(insertion_sort_for(arr))
print(insertion_sort_while(arr))
