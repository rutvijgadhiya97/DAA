import random

def insertion_sort(arr):
    # Insertion sort implementation
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
print("Insertion sort")
print("Default it takes random number from 1 to 100 depending on the size of the array you enter")
size= int(input("Enter the size of an Array: "))
arr=random.sample(range(0,101), size)
print("Array Before sort:")
print(arr)
sorted_array = insertion_sort(arr)
print("Array After sort:")
print(sorted_array)
