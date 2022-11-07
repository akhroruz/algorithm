# Selection Sort

def selection_sort_for(array: list[int]) -> list[int]:
    size = len(array)
    for i in range(size):
        min_index = i
        for m in range(min_index + 1, size):
            if array[m] < array[min_index]:
                min_index = m
                array[i], array[min_index] = array[min_index], array[i]
    return array


def selection_sort_while(array: list[int]) -> list[int]:
    i, m, size = 0, 1, len(array)
    while i < size:
        m = i + 1
        while m < size:
            if array[m] < array[i]:
                array[m], array[i] = array[i], array[m]
            m += 1
        i += 1
    return array


arr = [12, 11, 13, 5, 6]
print(selection_sort_for(arr))
print(selection_sort_while(arr))


