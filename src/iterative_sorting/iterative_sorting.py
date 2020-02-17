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

print(sorted_arr)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr