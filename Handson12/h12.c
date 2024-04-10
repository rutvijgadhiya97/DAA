#include <iostream>

class DynamicArray {
private:
    int* arr;
    int capacity;
    int size;

    void resize(int new_capacity) {
        int* new_arr = new int[new_capacity];
        for (int i = 0; i < size; ++i) {
            new_arr[i] = arr[i];
        }
        delete[] arr;
        arr = new_arr;
        capacity = new_capacity;
    }

public:
    DynamicArray() : arr(nullptr), capacity(0), size(0) {}

    ~DynamicArray() {
        delete[] arr;
    }

    void push_back(int value) {
        if (size >= capacity) {
            int new_capacity = (capacity == 0) ? 1 : capacity * 2;
            resize(new_capacity);
        }
        arr[size++] = value;
    }

    void pop_back() {
        if (size > 0) {
            --size;
        }
    }

    int& operator[](int index) {
        return arr[index];
    }

    int& front() {
        return arr[0];
    }

    int& back() {
        return arr[size - 1];
    }

    int getSize() const {
        return size;
    }

    int getCapacity() const {
        return capacity;
    }
};

int main() {
    DynamicArray dynArray;
    
    dynArray.push_back(10);
    dynArray.push_back(20);
    dynArray.push_back(30);
    
    std::cout << "Size: " << dynArray.getSize() << ", Capacity: " << dynArray.getCapacity() << std::endl;

    std::cout << "Elements: ";
    for (int i = 0; i < dynArray.getSize(); ++i) {
        std::cout << dynArray[i] << " ";
    }
    std::cout << std::endl;

    dynArray.pop_back();
    std::cout << "After popping back, Size: " << dynArray.getSize() << ", Capacity: " << dynArray.getCapacity() << std::endl;

    return 0;
}
