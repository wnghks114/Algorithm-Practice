arr = list(map(int, input().split()))
k = 1

for i in range(1, len(arr)) :
    if arr[i] != arr[k-1] :
        arr[k] = arr[i]
        k += 1

print(k)
print(arr[:k])