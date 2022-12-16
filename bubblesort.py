from random import randint
arr = []

for x in range (0, 11):
    arr.append(randint(1, 100))
print(arr)
for i in range (10):
    for j in range (10-i):
        if arr[j] > arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)