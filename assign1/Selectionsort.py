import random

def selection_sort(arr):
    # Selection sort implementation
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print("Selection sort")
print("Default it takes random number from 1 to 100 depending on the size of the array you enter")
size= int(input("Enter the size of an Array: "))
arr=random.sample(range(0,101), size)
print("Array Before sort:")
print(arr)
sorted_array = selection_sort(arr)
print("Array After sort:")
print(sorted_array)
