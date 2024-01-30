import time
import matplotlib.pyplot as plt
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

def selection_sort(arr):
    # Selection sort implementation
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    # Bubble sort implementation
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def generate_data(size):
    return random.sample(range(size * 10), size)

def benchmark_sorting_algorithm(sort_func, input_size):
    arr = generate_data(input_size)
    
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    
    return end_time - start_time

input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000]  # Add more as needed
sorting_algorithms = [insertion_sort, selection_sort, bubble_sort]
algorithm_names = ["Insertion Sort", "Selection Sort", "Bubble Sort"]

for i, sort_func in enumerate(sorting_algorithms):
    times = [benchmark_sorting_algorithm(sort_func, size) for size in input_sizes]

    # Plotting
    plt.plot(input_sizes, times, label=algorithm_names[i])

plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()
