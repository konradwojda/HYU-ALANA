def longest_increasing_subsequence(arr):
    lis_lengths = [1] * len(arr)
    previous = [-1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and lis_lengths[i] < lis_lengths[j] + 1:
                lis_lengths[i] = lis_lengths[j] + 1
                previous[i] = j

    max_length_index = lis_lengths.index(max(lis_lengths))

    lis = []
    current_index = max_length_index
    while current_index != -1:
        lis.append(arr[current_index])
        current_index = previous[current_index]

    lis.reverse()

    return lis

arr = [9, 44, 32, 12, 7, 42, 34, 92, 35, 37, 41, 8, 20, 27, 83, 64, 61, 28, 39, 
       93, 29, 17, 13, 14, 55, 21, 66, 72, 23, 73, 99, 1, 2, 88, 77, 3, 65, 83, 
       84, 62, 5, 11, 74, 68, 76, 78, 67, 75, 69, 70, 22, 71, 24, 25, 26]

lis = longest_increasing_subsequence(arr)

print("Longest increasing subsequence:", lis)
print(len(lis))