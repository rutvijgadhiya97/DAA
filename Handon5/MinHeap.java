package Handon5;


class GenericHeap<T extends Comparable<T>> {

    private T[] heapArray;
    private int heapSize;
    private int maxSize;

    private static final int ROOT_INDEX = 1;

    public GenericHeap(int maxSize) {
        this.maxSize = maxSize;
        this.heapSize = 0;
        heapArray = (T[]) new Comparable[this.maxSize + 1];
        heapArray[0] = null; // No need for Integer.MIN_VALUE in generic version
    }

    private int parentIndex(int pos) {
        return pos / 2;
    }

    private int leftChildIndex(int pos) {
        return (2 * pos);
    }

    private int rightChildIndex(int pos) {
        return (2 * pos) + 1;
    }

    private boolean isLeaf(int pos) {
        return pos > (heapSize / 2);
    }

    private void swap(int firstPos, int secondPos) {
        T temp = heapArray[firstPos];
        heapArray[firstPos] = heapArray[secondPos];
        heapArray[secondPos] = temp;
    }

    private void minHeapify(int pos) {
        if (!isLeaf(pos)) {
            int swapIndex = pos;
            if (rightChildIndex(pos) <= heapSize) {
                swapIndex = heapArray[leftChildIndex(pos)].compareTo(heapArray[rightChildIndex(pos)]) < 0 ?
                            leftChildIndex(pos) : rightChildIndex(pos);
            } else {
                swapIndex = leftChildIndex(pos);
            }

            if (heapArray[pos] == null || heapArray[swapIndex] == null) {
                return; // Handle null comparisons
            }

            if (heapArray[pos].compareTo(heapArray[swapIndex]) > 0) {
                swap(pos, swapIndex);
                minHeapify(swapIndex);
            }
        }
    }

    public void insert(T element) {
        if (heapSize >= maxSize) {
            return;
        }

        heapArray[++heapSize] = element;
        int current = heapSize;

        while (current > 1 && heapArray[current] != null && heapArray[parentIndex(current)] != null &&
                heapArray[current].compareTo(heapArray[parentIndex(current)]) < 0) {
            swap(current, parentIndex(current));
            current = parentIndex(current);
        }
    }

    public void print() {
        printTree(ROOT_INDEX, "");
    }

    private void printTree(int index, String prefix) {
        if (index <= heapSize) {
            printTree(rightChildIndex(index), prefix + "    ");
            System.out.println(prefix + "└── " + heapArray[index]);
            printTree(leftChildIndex(index), prefix + "    ");
        }
    }

    public T remove() {
        T popped = heapArray[ROOT_INDEX];
        heapArray[ROOT_INDEX] = heapArray[heapSize--];
        minHeapify(ROOT_INDEX);
        return popped;
    }

    public static void main(String[] args) {
        GenericHeap<Integer> intHeap = new GenericHeap<>(10);
        intHeap.insert(10);
        intHeap.insert(5);
        intHeap.insert(15);
        intHeap.insert(2);
        intHeap.insert(20);

        System.out.println("Min Heap of Integers:");
        intHeap.print();
        System.out.println("The Min val is " + intHeap.remove());
        intHeap.print();
        System.out.println();

        // Example with Float
        GenericHeap<Float> floatHeap = new GenericHeap<>(10);
        floatHeap.insert(10.5f);
        floatHeap.insert(5.2f);
        floatHeap.insert(15.8f);
        floatHeap.insert(2.1f);
        floatHeap.insert(20.7f);

        System.out.println("Min Heap of Floats:");
        floatHeap.print();
        System.out.println("The Min val is " + floatHeap.remove());
        floatHeap.print();
        System.out.println();

        // Example with custom object (Person)
        GenericHeap<Person> personHeap = new GenericHeap<>(10);
        personHeap.insert(new Person("Alice", 25));
        personHeap.insert(new Person("Bob", 30));
        personHeap.insert(new Person("Charlie", 20));
        personHeap.insert(new Person("David", 22));
        personHeap.insert(new Person("Eve", 28));

        System.out.println("Min Heap of Persons:");
        personHeap.print();
        System.out.println("The Min val is " + personHeap.remove());
        personHeap.print();
    }
}
