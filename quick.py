import random

# Deterministic quicksort
def partition_det(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def quicksort_det(arr, low, high):
    if low < high:
        pi = partition_det(arr, low, high)
        quicksort_det(arr, low, pi - 1)
        quicksort_det(arr, pi + 1, high)

# Randomized quicksort
def partition_ran(arr, low, high):
    randpivot = random.randrange(low, high)
    arr[low], arr[randpivot] = arr[randpivot], arr[low]
    return partition_det(arr, low, high)

def quicksort_ran(arr, low, high):
    if low < high:
        pi = partition_ran(arr, low, high)
        quicksort_ran(arr, low, pi - 1)
        quicksort_ran(arr, pi + 1, high)

# Test the functions
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort_det(arr, 0, n-1)
print("Sorted array using deterministic quicksort is:", arr)

arr = [10, 7, 8, 9, 1, 5]
quicksort_ran(arr, 0, n-1)
print("Sorted array using randomized quicksort is:", arr)
