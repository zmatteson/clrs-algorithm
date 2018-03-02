#Consider the searching problem
#Input: List of integers, and value v
#Output: An index i such that v = A[i] or -1 if v does not appear
#Code for linear search

def linear_search(A, v):
    for i in range(len(A)):
        if A[i] == v:
            return i
    return -1

if __name__ == "__main__":
    A = [1,2,3]
    print("A is ", A)
    print("The index of 4 in A is ", linear_search(A, 4))
    print("The index of 2 in A is ", linear_search(A,2))