//
// Created by zaids on 9/26/2025.
//

// Muhammad Zaid Saqib

// Lab practice

//Practice task 1
//The factorial of a number n (n!) is the product of all positive integers less than or equal to n.
/*
#include <iostream>
using namespace std;
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
int main() {
    int number;
    cout << "Enter a number to calculate its factorial: ";
    cin >> number;
    if (number < 0) {
        cout << "Factorial is not defined for negative numbers." << endl;
    } else {
        cout << "Factorial of " << number << " is " << factorial(number) << endl;
    }
    return 0;
}
*/

//Practise Task 2
// The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones.
// The sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on, with the rule being Fₙ = Fₙ₋₁ + Fₙ₋₂.
/*
#include<iostream>
using namespace std;

int fib(int n) {
    if(n==0 || n==1) {
        return n;
    }
    return fib(n-1) + fib(n-2);
}
int main() {
    int n;
    cout << "Enter the number of terms in the Fibonacci series: ";
    cin >> n;
    cout << "Fibonacci series up to " << n << " terms:" << endl;
    for(int i=0; i<n; i++) {
        cout << fib(i) << " ";
    }
    cout << endl;
    return 0;
}
*/

//Practice Task 3
//Lab Task 3: Counting Down
//A simple recursive function to count down from a number to 1.
/*
#include<iostream>
using namespace std;

void count(int n)
{
    if(n<1) {
        return;
    }
    cout << n << " ";
    count(n-1);
}
int main() {
    int number;
    cout << "Enter a number to count down from: ";
    cin >> number;
    cout << "Counting down from " << number << " to 1:" << endl;
    count(number);
    cout << endl;
    return 0;
}
*/

//Practice Task 4
//Reverse a String Using Recursion
/*
#include<iostream>
using namespace std;

void reversestring(string str)
{
    if(str.length() == 0) {
        return;
    }
    cout << str[str.length() - 1];
    reversestring(str.substr(0, str.length() - 1));
}
int main() {
    string input;
    cout << "Enter a string to reverse: ";
    cin >> input;
    cout << "Reversed string: ";
    reversestring(input);
    cout << endl;
    return 0;
}
*/


//Lab Task


//Q1Task 1: Print numbers from a given number down to 0 using recursion.
// Muhammad Zaid Saqib
/*
#include <iostream>
using namespace std;
void printDown(int n) {
    if (n < 0) {
        return;
    }
    cout << n << " ";
    printDown(n - 1);
}
int main() {
    int number;
    cout << "Enter a number: ";
    cin >> number;
    cout << "Numbers from " << number << " down to 0 are:" << endl;
    printDown(number);
    cout << endl;
    return 0;
}
*/


//Q2Task 2: Check if a string is a palindrome using recursion. (Like Madam and madam are same even after reversing a
//string, 1011 becomes 1101 after reversing which is not the same number so it is not palindrome.)
// Muhammad Zaid Saqib
/*
#include <iostream>
using namespace std;
bool isPalindrome(const string &str, int left, int right) {
    if (left >= right) {
        return true;
    }
    if (str[left] != str[right]) {
        return false;
    }
    return isPalindrome(str, left + 1, right - 1);
}
int main() {
    string input;
    cout << "Enter a string: ";
    cin >> input;
    if (isPalindrome(input, 0, input.length() - 1)) {
        cout << input << " is a palindrome." << endl;
    } else {
        cout << input << " is not a palindrome." << endl;
    }
    return 0;
}
*/

//Q3Task 3: Calculate the sum of elements in an array using recursion.
// Muhammad Zaid Saqib
/*
#include<iostream>
using namespace std;
int sumArray(int arr[], int n) {
    if (n == 0) return 0;
    return arr[n - 1] + sumArray(arr, n - 1);

}
int main() {
    int n;
    cout << "Enter the number of elements in the array: ";
    cin >> n;
    int arr[n];
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int sum = sumArray(arr, n);
    cout << "The sum of the elements in the array is: " << sum << endl;
    return 0;
}
    */