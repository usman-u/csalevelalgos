


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
print(recur_binary_search(sorted_data, 16, 0, len(sorted_data)-1))
print(binary_search(sorted_data, 16))