def CountingSort(A, B, k):
    # Create and initialize C array
    C = [0] * (k + 1)
    for x in range(k + 1):
        C[k] = 0
    
    # Compute the count of each element in A
    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1
    
    # Compute C[x] == count of A[j] <= x
    for i in range(1, (k + 1)):
        C[i] = C[i] + C[i - 1]

    # Place each A[j] in sorted order in B starting from the end
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

# test
arr = [3, 1, 3, 0, 1, 0, 1, 2, 3, 4, 5, 0, 2]
res = [0] * (len(arr))
CountingSort(arr, res, 5)
print("Initial array: " + str(arr))
print("Sorted array: " + str(res))