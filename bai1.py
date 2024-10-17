def sort_colors(arr):
    low = 0      
    mid = 0       
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 'đỏ':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'trắng':
            mid += 1
        else:

            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

input_str = input()
arr = input_str.split()

sorted_arr = sort_colors(arr)
print(sorted_arr)
