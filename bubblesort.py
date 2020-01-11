# Python program for bubble sort
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# array example to check the code
a = [20, 5, 87, 48, 66]
print("Array before Bubble sort")
for i in range(len(a)):
    print("%d" %a[i])
bubble(a)
print("Array after Bubble sort")
for i in range(len(a)):
    print("%d" %a[i])
