def selection_sort(A):
    for j in range(len(A)):
        min_index = j
        for i in range(j+1, len(A)):
            if A[min_index] > A[i]:
                min_index = i
        temp = A[j]
        A[j] = A[min_index]
        A[min_index] = temp
    return A

if __name__ == "__main__":
    A = [9,5,4,1]
    print(A)
    print(selection_sort(A))