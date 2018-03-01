def heapify(A):
    n = len(A)
    i = len(A) // 2 - 1
    while i >= 0:
        sift_down(A, n, i)
        i -= 1


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


def heap_maximum(A):
    return A[0]
#O(1) time

def heap_extract_max(A):
    if len(A) < 1:
        return None
    m = A[0]
    A[0] = A[len(A)-1]
    A.pop(len(A)-1)
    sift_down(A, len(A), 0)
    return m    
#O(log n)

def heap_increase_key(A, i, key):
    if key < A[i]:
        raise ValueError('new key is smaller than current key')
    A[i] = key
    while i > 0 and A[i//2] < A[i]:
        A[i], A[i//2] = A[i//2], A[i]
        i = i//2
#Running time O(log n)

def max_heap_insert(A, key):
    A.append(float('-inf'))
    heap_increase_key(A, len(A)-1, key)
# Running time O(log n)

if __name__ == "__main__":
    A = [10,51,30,1,2,0,12]
    print(A)
    heapify(A)
    print(A)
    print("heap_max(A) returns: ", heap_maximum(A))
    print("heap_extract_max(A) returns: ", heap_extract_max(A))
    print("A is now: ", A)
    heap_increase_key(A, 3, 100)
    print("heap_increase_key(A, 3, 100) modifies A : ", A)
    max_heap_insert(A, 6)
    print("max_heap_insert(A, 6) modifies A : ", A)