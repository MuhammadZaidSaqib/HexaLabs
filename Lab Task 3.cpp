//
// Created by zaids on 9/20/2025.
//

//Q1 Write a program on c++ that takes age of five persons and
// then just display the age of each person by using arrays.

/*#include <iostream>
using namespace std;
int main() {
    int ages[5];


    for (int i = 0; i < 5; i++) {
        cout << "Enter age of person " << (i + 1) << ": ";
        cin >> ages[i];
    }


    cout << "\nAges of the persons are:\n";
    for (int i = 0; i < 5; i++) {
        cout << "Age of person " << (i + 1) << ": " << ages[i] << endl;
    }

    return 0;
}*/


//Q2.	Write a c++ program to ask users to create a 1D array of 10 elements and
// then create a function to count even and odd numbers present in the array
// and display the count values along with the elements.

/*#include <iostream>
using namespace std;
void countEvenOdd(int arr[], int size, int &evenCount, int &oddCount) {
    evenCount = 0;
    oddCount = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] % 2 == 0) {
            evenCount++;
        } else {
            oddCount++;
        }
    }
}
int main() {
    const int size = 10;
    int arr[size];
    int evenCount, oddCount;
    cout << "Enter 10 elements for the array:\n";
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }
    countEvenOdd(arr, size, evenCount, oddCount);
    cout << "Even numbers count: " << evenCount << endl;
    cout << "Odd numbers count: " << oddCount << endl;
    return 0;
}*/

//Q3 Write a c++ program to create a 1D array and create a function to find the largest
//and smallest element in the array.

/*
#include<iostream>
using namespace std;
void findLargestSmallest(int arr[], int size, int &largest, int &smallest
) {
    largest = arr[0];
    smallest = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
        if (arr[i] < smallest) {
            smallest = arr[i];
        }
    }
}
int main() {
    const int size = 5;
    int arr[size];
    int largest, smallest;
    cout << "Enter " << size << " elements for the array:\n";
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }
    findLargestSmallest(arr, size, largest, smallest);
    cout << "Largest element: " << largest << endl;
    cout << "Smallest element: " << smallest << endl;
    return 0;
}*/

//Q4 Write a program in C++, to input data into an array. Enter a value from the Keyboard and
//find out the location of the entered value in the array. If the entered number is found in the array,
//display the message "Number Found―else display ―Number Not Found‖

/*
#include<iostream>
using namespace std;

int main() {
    const int size = 5;
    int arr[size];
    int value, location = -1;

    cout << "Enter " << size << " elements for the array:\n";
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }

    cout << "Enter a value to search in the array: ";
    cin >> value;

    for (int i = 0; i < size; i++) {
        if (arr[i] == value) {
            location = i;
            break;
        }
    }

    if (location != -1) {
        cout << "Number Found at location " << (location + 1) << endl;
    } else {
        cout << "Number Not Found" << endl;
    }

    return 0;
}*/

//Q5 Develop a program that takes 5 array elements from user.
// Swap position [2] element with position [4] element.

/*
#include<iostream>
using namespace std;
int main() {
    const int size = 5;
    int arr[size];

    cout << "Enter " << size << " elements for the array:\n";
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }


    int temp = arr[1];
    arr[1] = arr[3];
    arr[3] = temp;

    cout << "Array after swapping elements at position 2 and 4:\n";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
*/


