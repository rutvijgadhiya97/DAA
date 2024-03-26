import java.util.Arrays;
import java.util.Scanner;

class Node<K, V> {
    K key;
    V value;
    Node<K, V> next;
    Node<K, V> prev;

    public Node(K key, V value) {
        this.key = key;
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

public class HashTable<K, V> {
    private static final int DEFAULT_CAPACITY = 16;
    private static final double LOAD_FACTOR = 0.75;
    private static final double SHRINK_FACTOR = 0.25;

    private Node<K, V>[] table;
    private int size;

    public HashTable() {
        table = new Node[DEFAULT_CAPACITY];
        size = 0;
    }

    private int hash(K key) {
        int hash = key.hashCode();
        return (int) (table.length * ((hash * 0.6180339887) % 1));
    }

    public void put(K key, V value) {
        int index = hash(key);
        Node<K, V> newNode = new Node<>(key, value);

        if (table[index] == null) {
            table[index] = newNode;
        } else {
            Node<K, V> current = table[index];
            while (current.next != null) {
                if (current.key.equals(key)) {
                    current.value = value;
                    return;
                }
                current = current.next;
            }
            current.next = newNode;
            newNode.prev = current;
        }
        size++;

        if ((double) size / table.length >= LOAD_FACTOR) {
            resize(table.length * 2);
        }
    }

    public V get(K key) {
        int index = hash(key);
        Node<K, V> current = table[index];

        while (current != null) {
            if (current.key.equals(key)) {
                return current.value;
            }
            current = current.next;
        }
        return null;
    }

    public void remove(K key) {
        int index = hash(key);
        Node<K, V> current = table[index];

        while (current != null) {
            if (current.key.equals(key)) {
                if (current.prev != null) {
                    current.prev.next = current.next;
                } else {
                    table[index] = current.next;
                }
                if (current.next != null) {
                    current.next.prev = current.prev;
                }
                size--;

                if ((double) size / table.length <= SHRINK_FACTOR) {
                    resize(table.length / 2);
                }
                return;
            }
            current = current.next;
        }
    }

    private void resize(int newCapacity) {
        Node<K, V>[] newTable = new Node[newCapacity];
        for (int i = 0; i < table.length; i++) {
            Node<K, V> current = table[i];
            while (current != null) {
                Node<K, V> next = current.next;
                int newIndex = hash(current.key);
                if (newTable[newIndex] == null) {
                    newTable[newIndex] = current;
                    current.prev = null;
                    current.next = null;
                } else {
                    current.next = newTable[newIndex];
                    newTable[newIndex].prev = current;
                    newTable[newIndex] = current;
                }
                current = next;
            }
        }
        table = newTable;
    }
    public void printTable() {
        for (int i = 0; i < table.length; i++) {
            System.out.print("Bucket " + i + ": ");
            Node<K, V> current = table[i];
            while (current != null) {
                System.out.print("(" + current.key + ", " + current.value + ") ");
                current = current.next;
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        HashTable<Integer, Integer> ht = new HashTable<>();
        Scanner scanner = new Scanner(System.in);
        char choice;

        do {
            System.out.println("Choose an operation:");
            System.out.println("1. Insert");
            System.out.println("2. Remove");
            System.out.println("3. Print Table");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.next().charAt(0);

            switch (choice) {
                case '1':
                    System.out.print("Enter key: ");
                    int key = scanner.nextInt();
                    System.out.print("Enter value: ");
                    int value = scanner.nextInt();
                    ht.put(key, value);
                    break;
                case '2':
                    System.out.print("Enter key to remove: ");
                    int removeKey = scanner.nextInt();
                    ht.remove(removeKey);
                    break;
                case '3':
                    ht.printTable();
                    break;
                case '4':
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice! Please try again.");
            }
        } while (choice != '4');

        scanner.close();
    }
}
