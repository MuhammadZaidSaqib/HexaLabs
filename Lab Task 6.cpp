//
// Created by zaids on 10/11/2025.
//


// Task 1: Linear Search Implementation
//Write a C++ program that uses linear search to find a user-input value in the following dataset:
//int data1[] = {5, 2, 9, 1, 7};

/*
#include<iostream>
using namespace std;
int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}
int main() {
    int data1[] = {5, 2, 9, 1, 7};
    int size = sizeof(data1) / sizeof(data1[0]);
    int target;

    cout << "Enter a number to search: ";
    cin >> target;

    int result = linearSearch(data1, size, target);

    if (result != -1) {
        cout << "Element found at index: " << result << endl;
    } else {
        cout << "Element not found in the array." << endl;
    }

    return 0;
}
*/

// Task 2: Binary Search Implementation
//Write a C++ program that uses **binary search** to find a user-input value in the following dataset:
//int data2[] = {1, 3, 5, 7, 9};
/*
#include<iostream>
using namespace std;
int binarySearch(int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            return mid;
        }
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}
int main() {
    int data2[] = {1, 3, 5, 7, 9};
    int size = sizeof(data2) / sizeof(data2[0]);
    int target;
    cout << "Enter a number to search: ";
    cin >> target;
    int result = binarySearch(data2, size, target);
    if (result != -1) {
        cout << "Element found at index: " << result << endl;
    } else {
        cout << "Element not found in the array." << endl;
    }
    return 0;
}
*/