def counting_sort(A):
    k = max(A)
    C = [0] * (k + 1)
    B = ["_"] * len(A)

    print(f"Array A: {A}")
    
    for a in A:
        C[a] += 1
    
    print(f"Array C containing number of elements equal to i: {C}")

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    print(f"Array C contains the number of elements less than or equal to i: {C}")

    
    for i, a in enumerate(reversed(A)):
        B[C[a] - 1] = a
        C[a] -= 1
        print(f"{i+1}.")
        print(f"B : {B}")
        print(f"C : {C}")
    
    return B

A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
print(counting_sort(A))
