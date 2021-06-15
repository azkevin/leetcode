import random

def HeapSort(A):
    buildMinHeap(A)
    n = len(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        minHeapify(A, 0, i)

def buildMinHeap(A):
    n = len(A)
    for i in range((n // 2) - 1, -1, -1):
        minHeapify(A, i, n)

def minHeapify(A, i, n):
    left = (2 * i) + 1
    right = (2 * i) + 2
    smallest = i
    if left < n and A[left] < A[i]:
        smallest = left
    if right < n and A[right] < A[smallest]:
        smallest = right
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        minHeapify(A, smallest, n)

# Test run using an array of 10 random numbers with values from 1 to 10
A = random.sample(range(1, 11), 10)
print("Initial array: " + str(A))
HeapSort(A)
print("Sorted array: " + str(A))