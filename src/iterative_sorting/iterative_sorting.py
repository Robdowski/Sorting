# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    for i in range(len(arr)):
        smallest_value_index = i 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_value_index]:
                smallest_value_index = j
                
        arr[i], arr[smallest_value_index] = arr[smallest_value_index], arr[i]

    return arr

sorty = [1, 4, 3, 2, 5]

sorted_arr = selection_sort(sorty)

print('Sorted Selection', sorted_arr)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped=False
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True

        if swapped == False:
            break
    return arr

bubbly = [2, 3, 1, 5, 4]

sorted_bubble = bubble_sort(bubbly)

print('Sorted Bubble', sorted_bubble)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    count = {}
    next_index = []
    sorted_arr = []
    for item in arr:
        count[item] += 1
    return arr