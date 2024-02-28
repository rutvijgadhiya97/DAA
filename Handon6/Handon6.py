import matplotlib.pyplot as plt
import time
import random
import sys

sys.setrecursionlimit(10**6)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort_non_random(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_non_random(arr, low, pi-1)
        quicksort_non_random(arr, pi+1, high)

def benchmark_quicksort(array_sizes):
    best_case_times = []
    worst_case_times = []
    average_case_times = []

    for n in array_sizes:
        # Best case: Array is already sorted
        best_case_arr = list(range(n))
        start_time = time.time()
        quicksort_non_random(best_case_arr, 0, n-1)
        best_case_time = time.time() - start_time
        best_case_times.append(best_case_time)

        # Worst case: Array is sorted in reverse order
        worst_case_arr = list(range(n, 0, -1))
        start_time = time.time()
        quicksort_non_random(worst_case_arr, 0, n-1)
        worst_case_time = time.time() - start_time
        worst_case_times.append(worst_case_time)

        # Average case: Array elements are randomly distributed
        average_case_arr = [random.randint(0, n-1) for _ in range(n)]
        start_time = time.time()
        quicksort_non_random(average_case_arr, 0, n-1)
        average_case_time = time.time() - start_time
        average_case_times.append(average_case_time)

        # Print the times for this array size
        print(f"Array Size: {n}")
        print(f"Best Case Time: {best_case_time:.6f} seconds")
        print(f"Worst Case Time: {worst_case_time:.6f} seconds")
        print(f"Average Case Time: {average_case_time:.6f} seconds")
        print("-" * 40)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(array_sizes, best_case_times, label='Best Case', marker='o')
    plt.plot(array_sizes, worst_case_times, label='Worst Case', marker='s')
    plt.plot(array_sizes, average_case_times, label='Average Case', marker='^')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Non-random Pivot Quicksort Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

# Define the array sizes for benchmarking
array_sizes = [100, 200, 300, 400, 1000,5000,10000]
benchmark_quicksort(array_sizes)
