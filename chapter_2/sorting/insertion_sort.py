def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        #Insert A[j] into the sorted sequence A[0..j-1]
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

if __name__ == "__main__":
    A = [4,1,6,10,9]
    print(A)
    print(insertion_sort(A))