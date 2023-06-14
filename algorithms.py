
sorted_data = [1, 4, 6, 8, 10, 12, 14, 16, 18]
unsorted_data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -100, 121221]


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

# print(bubble_sort(unsorted_data))


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

def quick_sort(data, start, end):
    # Base case; where list size is 1 or greater (where start >= end)
    if start <= end:
        # Split = the index of the pivot of the partitioned data
        split = partition(data, start, end)
        
        # Recursively call QS on the left and right of the list
        # split index -/+ 1, since not including the previous pivot
        quick_sort(data, start, split-1)
        quick_sort(data, split+1, end)
    return data

# Partitions the data, such that all values left of the pivot are smaller than the pivot value, and vice versa
# Returns pivot index
def partition(data, start, end):
    pivotValue = data[start]
    left = start + 1
    right = end

    while left <= right:
        
        while left <= right and data[left] <= pivotValue:
            left += 1

        while left <= right and data[right] >= pivotValue:
            right -= 1
            
        # If above criteria met (pointers haven't crossed over)
        # Swap the values are the right and left pointers
        if left <= right:
            tmp = data[left]
            data[left] = data[right]
            data[right] = tmp
    
    # After the pointers have crossed over (as left is not less than right)
    # Swap the pivot value with the value at the right pointer
    # Where start = pivot
    data[start] = data[right]
    data[right] = pivotValue
    
    # Reuturn pivot index
    return right

print(quick_sort(unsorted_data, 0, len(unsorted_data)-1))