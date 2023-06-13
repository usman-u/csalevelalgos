


def binary_search(data, item):
    start = 0
    end = len(data)-1

    while start <= end:
        # DIV (floor division, disregards remainder)
        mid = (start + end) // 2           

        if data[mid] == item:
            return mid

        if data[mid] > item:
            end = mid - 1
        
        if data[mid] < item:
            start = mid + 1

    return -1


def recur_binary_search(data, item, start, end):
    # base case, -1 is absent
    if start > end:
        return -1

    # DIV (floor division, disregards remainder)
    mid = (start + end) // 2 
    
    if data[mid] > item:
        return recur_binary_search(data, item, start, mid-1)
    
    if data[mid] < item:
        return recur_binary_search(data, item, mid+1, end)
    
    return mid


sorted_data = [1, 4, 6, 8, 10, 12, 14, 16, 18]

# print(recur_binary_search(sorted_data, 16, 0, len(sorted_data)-1))
# print(binary_search(sorted_data, 16))


#   O(n^2) time complexity
#   optimised with n, to reduce needless passes over sorted part of data
def bubble_sort(data):
    swapped = True
    n = 0
    while swapped == True and n < len(data)-1:
        swapped = False
        for j in range(0, len(data)-1-n):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
                swapped = True
        n += 1
    return data

unsorted_data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -100, 121221]
print(bubble_sort(unsorted_data))


def insertion_sort(data):
    for i in range(0, len(data)-1):
        current_data = data[i]
        position = i

        while position > 0 and data[position-1] > current_data:
            data[position] = data[position-1]
            position -= 1
        data[position] = current_data
    return data

# print(insertion_sort(unsorted_data))