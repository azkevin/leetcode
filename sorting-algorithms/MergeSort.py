import random

def MergeSort(A, lo, hi):
    if lo < hi:   
        mid = (lo + hi) // 2    # floor div is used to remove potential decimals
        MergeSort(A, lo, mid) 
        MergeSort(A, mid + 1, hi)
        merge(A, lo, mid, hi) 

def merge(A, lo, mid, hi): 
    n1 = mid - lo + 1
    n2 = hi - mid 
   
    L = [0] * n1                # Create L[0..n1]
    R = [0] * n2                # Create R[0..n2]
  
    for i in range(0, n1): 
        L[i] = A[lo + i]
    for j in range(0, n2):
        R[j] = A[mid + j + 1]
  
    i = j = 0
    k = lo
  
    while i < n1 and j < n2: 
        if L[i] <= R[j]:        # copy the smaller of L[i] and R[j] to A[k]
            A[k] = L[i] 
            i += 1
        else: 
            A[k] = R[j] 
            j += 1
        k += 1    
    while i < n1: 
        A[k] = L[i]             # if R is exhausted then copy L[i] to A[k]
        i += 1
        k += 1
    while j < n2: 
        A[k] = R[j]             # if L is exhausted then copy R[j] to A[k]
        j += 1
        k += 1
  
# Test run using an array of 10 random numbers with values from 1 to 10
A = random.sample(range(1, 11), 10)
print("Initial array: " + str(A))
MergeSort(A, 0, len(A)-1) 
print("Sorted array: " + str(A))