import random

def QuickSort(A, lo, hi):
    if lo < hi:
        mid = partition(A, lo, hi)
        QuickSort(A, lo, mid - 1)
        QuickSort(A, mid + 1, hi)

def partition(A, lo, hi):
    pivot = A[hi]
    i = lo - 1
    for j in range(lo, hi):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[hi] = A[hi], A[i + 1]
    return i + 1

# Test run using an array of 10 random numbers with values from 1 to 10
arr = random.sample(range(1, 11), 10)
print("Initial array: " + str(arr))
QuickSort(arr, 0, len(arr) - 1)
print("Sorted array: " + str(arr))