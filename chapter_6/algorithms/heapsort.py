def heapsort(A):
    heapify(A)
    i = len(A) - 1
    while i > 0:
        A[0], A[i] = A[i], A[0]
        sift_down(A, i, 0)
        i -= 1
#Running time : O (n * log n)

def sift_down(A, n, i):
    largest = i
    l = 2*i + 1 
    r = 2*i + 2
    if l < n and A[l] > A[i]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest] , A[i]
        sift_down(A, n, largest)

#Max_heapify running time: T(n) <= T(2n/3) + Theta(1)
#O(log n) or O(height)

def heapify(A):
    n = len(A)
    i = len(A) // 2 - 1
    while i >= 0:
        sift_down(A, n, i)
        i -= 1
# Build max_head running time : O(n)

if __name__ == "__main__":
    A = [10,51,30,1,2,0,12]
    print(A)
    heapsort(A)
    print(A)
