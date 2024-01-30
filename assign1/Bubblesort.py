import random

def bubble_sort(arr):
    # Bubble sort implementation
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print("Bubble sort")
print("Default it takes random number from 1 to 100 depending on the size of the array you enter")
size= int(input("Enter the size of an Array: "))
arr=random.sample(range(0,101), size)
print("Array Before sort:")
print(arr)
sorted_array = bubble_sort(arr)
print("Array After sort:")
print(sorted_array)
