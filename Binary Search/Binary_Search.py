def binary_search(element, some_list):
    if some_list[0] > element or some_list[len(some_list) - 1] < element:
        return None

    start = 0
    last = len(some_list) - 1
    while start <= last:
        middle = (start + last)//2
       	if some_list[middle] == element:
            return middle
        elif some_list[middle] > element:
        	last = middle - 1
        else:
            start = middle + 1

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))