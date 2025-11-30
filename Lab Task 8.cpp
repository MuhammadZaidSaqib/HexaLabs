//
// Created by zaids on 11/2/2025.
//


//Task 4: Hybrid Insertion Sort
//Implement a modified version that stops the inner loop early if no swaps were made in a complete pass (indicating the array is already sorted).
//Compare its performance with the standard version on a nearly sorted array.
/*
#include<iostream>
using namespace std;
void hybridInsertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        bool swapped = false;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
            swapped = true;
        }
        arr[j + 1] = key;

        // If no swaps were made, the array is already sorted
        if (!swapped) {
            break;
        }
    }
}
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}
int main() {
    int arr[] = {1, 2, 3, 5, 4, 6, 7, 8, 9, 10}; // Nearly sorted array
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    printArray(arr, n);

    hybridInsertionSort(arr, n);

    cout << "Sorted array: ";
    printArray(arr, n);
    return 0;
}
*/

//Modify the insertion sort algorithm to sort an array in descending order instead of ascending order. Test it with the array: `{31, 41, 59, 26, 41, 58}`
/*
#include <iostream>
using namespace std;
void insertionSortDescending(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        // Move elements of arr[0..i-1], that are less than key,
        // to one position ahead of their current position
        while (j >= 0 && arr[j] < key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}
int main() {
    int arr[] = {31, 41, 59, 26, 41, 58};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "Original array: ";
    printArray(arr, n);
    insertionSortDescending(arr, n);
    cout << "Sorted array in descending order: ";
    printArray(arr, n);
    return 0;
}*/

//Task 3
//Write a program that uses insertion sort to sort an array of strings in alphabetical order. Use the following test data:
//`{"banana", "apple", "cherry", "date", "blueberry"}`
/*
#include <iostream>
#include <string>
using namespace std;
void insertionSortStrings(string arr[], int n) {
    for (int i = 1; i < n; i++) {
        string key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
void printArray(string arr[], int n) {
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}
int main() {
    string arr[] = {"banana", "apple", "cherry", "date", "blueberry"};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "Original array: ";
    printArray(arr, n);
    insertionSortStrings(arr, n);
    cout << "Sorted array in alphabetical order: ";
    printArray(arr, n);
    return 0;
}*/

//Task 4: Hybrid Insertion Sort
//Implement a modified version that stops the inner loop early if no swaps were made in a complete pass (indicating the array is already sorted).
//Compare its performance with the standard version on a nearly sorted array.
/*
#include<iostream>
using namespace std;
void standardInsertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
void hybridInsertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        bool swapped = false;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
            swapped = true;
        }
        arr[j + 1] = key;
        if (!swapped) {
            break;
        }
    }
}
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}
int main() {
    int arr1[] = {1, 2, 3, 5, 4, 6, 7, 8, 9, 10};
    int arr2[] = {1, 2, 3, 5, 4, 6, 7, 8, 9, 10};
    int n = sizeof(arr1) / sizeof(arr1[0]);
    cout << "Original array for standard insertion sort: ";
    printArray(arr1, n);
    standardInsertionSort(arr1, n);
    cout << "Sorted array using standard insertion sort: ";
    printArray(arr1, n);
    cout << "Original array for hybrid insertion sort: ";
    printArray(arr2, n);
    hybridInsertionSort(arr2, n);
    cout << "Sorted array using hybrid insertion sort: ";
    printArray(arr2, n);
    return 0;
}*/

//Example 2
/*
#include <iostream>
using namespace std;
int binarySearchInsert(int arr[], int left, int right, int key) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] <= key)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return left;
}
void binaryInsertionSortWithSteps(int arr[], int n) {
    cout << "Sorting Process (binary insertion):\n\n";
    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int pos = binarySearchInsert(arr, 0, i - 1, key);
        cout << "Pass " << i << ": key=" << key << ", insert_at=" << pos << '\n';
        for (int j = i - 1; j >= pos; --j)
            arr[j + 1] = arr[j];
        arr[pos] = key;
        cout << "After insertion: ";
        for (int k = 0; k < n; ++k) cout << arr[k] << ' ';
        cout << "\n\n";
    }
}
int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    for (int i = 0; i < n; ++i) cout << arr[i] << ' ';
    cout << "\n\n";

    binaryInsertionSortWithSteps(arr, n);

    cout << "Final sorted array: ";
    for (int i = 0; i < n; ++i) cout << arr[i] << ' ';
    cout << '\n';
    return 0;
}*/

// Example 3
/*#include <iostream>
#include <string>
using namespace std;

int main() {
    char word[] = "insertion";
    string s(word);

    cout << "Original word: " << s << endl;

    const int ALPH = 26;
    int freq[ALPH] = {0};
    for (char c : s) {
        if (c >= 'a' && c <= 'z') ++freq[c - 'a'];
        else ++freq[0]; // fallback (optional)
    }

    string sorted;
    sorted.reserve(s.size());
    for (int i = 0; i < ALPH; ++i)
        sorted.append(freq[i], char('a' + i));

    cout << "Sorted characters: " << sorted << endl;
    return 0;
}
*/
