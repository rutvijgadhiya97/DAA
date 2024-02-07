def custom_merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left_half = array[:middle]
        right_half = array[middle:]

        custom_merge_sort(left_half)
        custom_merge_sort(right_half)

        left_index = right_index = array_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                array[array_index] = left_half[left_index]
                left_index += 1
            else:
                array[array_index] = right_half[right_index]
                right_index += 1
            array_index += 1

        while left_index < len(left_half):
            array[array_index] = left_half[left_index]
            left_index += 1
            array_index += 1

        while right_index < len(right_half):
            array[array_index] = right_half[right_index]
            right_index += 1
            array_index += 1

    

if __name__ == "__main__":

    input_array = [5, 2, 4, 7, 1, 3, 2, 6]
    print("Original array:", input_array)
    custom_merge_sort(input_array)
    print("Sorted array:", input_array)
