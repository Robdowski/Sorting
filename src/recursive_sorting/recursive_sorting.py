# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arr, arrA, arrB ):
    i = 0
    j = 0
    k = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            arr[k] = arrA[i]
            i += 1
        else:
            arr[k] = arrB[j]
            j += 1
        k += 1

    while i < len(arrA):
        arr[k] = arrA[i]
        i += 1
        k += 1

    while j < len(arrB):
        arr[k] = arrB[j]
        j += 1
        k += 1

    return arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    mid = len(arr)//2
    if len(arr) > 1:
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)
    
    return arr

arr_to_sort = [5, 4, 2, 1, 3, 9, 0, 7, 6, 8]

print(merge_sort(arr_to_sort))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
