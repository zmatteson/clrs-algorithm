#Add 2 n bit binary integers, stored in two n-element arrays
#The sum should be stored in binary form in an (n + 1) array C
#Input 2 Arrays of size n representing binary ints
#Output one array of their sum with size n+1

def add_binary_ints(A,B):
    C = []
    carry = 0
    for i in range(len(A)-1, -1, -1):
        s = A[i] + B[i]
        if s > 1:
            C.insert(0,0)
            carry = 1
        elif s + carry > 1:
            C.insert(0,0)
            carry = 1
        else:
            C.insert(0,s+carry)
            carry = 0
    if carry == 1:
        C.insert(0, carry)
    else:
        C.insert(0,0)
            
    return C
if __name__ == "__main__":
    print(add_binary_ints([1,1,1],[0,0,1]))