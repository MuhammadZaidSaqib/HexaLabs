//
// Created by zaids on 11/2/2025.
//

/*Task 1: Simple Customer Service Simulator
Create a program that simulates a customer service queue. The user can:
1.	Add a customer (enqueue a customer ID or name).
2.	Serve the next customer (dequeue and display who is being served).
3.	View the next customer (peek without serving).
4.	Display the current queue size.
Keep the program running in a loop until the user chooses to exit
*/
/*
#include <iostream>
#include <queue>
#include <string>
using namespace std;
void displayMenu() {
    cout << "\nCustomer Service Queue Simulator\n";
    cout << "1. Add a customer\n";
    cout << "2. Serve the next customer\n";
    cout << "3. View the next customer\n";
    cout << "4. Display current queue size\n";
    cout << "5. Exit\n";
    cout << "Choose an option (1-5): ";
}
int main() {
    queue<string> customerQueue;
    int choice;
    string customerName;

    do {
        displayMenu();
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter customer name or ID: ";
                cin >> ws; // Clear leading whitespace
                getline(cin, customerName);
                customerQueue.push(customerName);
                cout << "Customer " << customerName << " added to the queue.\n";
                break;
            case 2:
                if (!customerQueue.empty()) {
                    cout << "Serving customer: " << customerQueue.front() << "\n";
                    customerQueue.pop();
                } else {
                    cout << "No customers in the queue.\n";
                }
                break;
            case 3:
                if (!customerQueue.empty()) {
                    cout << "Next customer to be served: " << customerQueue.front() << "\n";
                } else {
                    cout << "No customers in the queue.\n";
                }
                break;
            case 4:
                cout << "Current queue size: " << customerQueue.size() << "\n";
                break;
            case 5:
                cout << "Exiting the program. Goodbye!\n";
                break;
            default:
                cout << "Invalid option! Please choose between 1 and 5.\n";
        }
    } while (choice != 5);

    return 0;
}
*/

/*
Task 2:
Circular Queue Implementation (Array-Based)
Modify the array-based queue example to be a circular queue explicitly, if you haven't already. Write a function void displayQueue()
that prints all the elements currently in the queue from front to rear. Handle the wrap-around condition properly.
 */
/*
 #include<iostream>
 using namespace std;
 #define MAX 5
    class CircularQueue {
        int front, rear;
        int arr[MAX];
    public:
        CircularQueue() {
            front = -1;
            rear = -1;
        }
        bool isFull() {
            return (front == 0 && rear == MAX - 1) || (front == rear + 1);
        }
        bool isEmpty() {
            return front == -1;
        }
        void enqueue(int element) {
            if (isFull()) {
                cout << "Queue is full. Cannot enqueue " << element << ".\n";
                return;
            }
            if (isEmpty()) {
                front = 0;
            }
            rear = (rear + 1) % MAX;
            arr[rear] = element;
            cout << element << " enqueued to the queue.\n";
        }
        void dequeue() {
            if (isEmpty()) {
                cout << "Queue is empty. Cannot dequeue.\n";
                return;
            }
            cout << arr[front] << " dequeued from the queue.\n";
            if (front == rear) {
                front = -1;
                rear = -1;
            } else {
                front = (front + 1) % MAX;
            }
        }
        void displayQueue() {
            if (isEmpty()) {
                cout << "Queue is empty.\n";
                return;
            }
            cout << "Queue elements: ";
            int i = front;
            while (true) {
                cout << arr[i] << " ";
                if (i == rear) break;
                i = (i + 1) % MAX;
            }
            cout << "\n";
        }
    };
    int main() {
        CircularQueue cq;
        cq.enqueue(10);
        cq.enqueue(20);
        cq.enqueue(30);
        cq.displayQueue();
        cq.dequeue();
        cq.displayQueue();
        cq.enqueue(40);
        cq.enqueue(50);
        cq.enqueue(60);
        cq.displayQueue();
        cq.enqueue(70); // This should show queue is full
        cq.dequeue();
        cq.displayQueue();
        return 0;
    }
 */

/* Task 3:
Deque (Double Ended Queue) using Linked List

Implement a Deque (Double Ended Queue) using a doubly linked list. A deque allows insertion and deletion from both ends. Your implementation should include:
•	insertFront(int data)
•	insertRear(int data)
•	deleteFront()
•	deleteRear()
•	getFront()
•	getRear()
•	isEmpty()
*/
/*
#include <iostream>
using namespace std;
class Node {
public:
    int data;
    Node* next;
    Node* prev;
    Node(int val) : data(val), next(nullptr), prev(nullptr) {}
};
class Deque {
private:
    Node* front;
    Node* rear;
public:
    Deque() : front(nullptr), rear(nullptr) {}
    bool isEmpty() {
        return front == nullptr;
    }
    void insertFront(int data) {
        Node* newNode = new Node(data);
        if (isEmpty()) {
            front = rear = newNode;
        } else {
            newNode->next = front;
            front->prev = newNode;
            front = newNode;
        }
        cout << data << " inserted at front.\n";
    }
    void insertRear(int data) {
        Node* newNode = new Node(data);
        if (isEmpty()) {
            front = rear = newNode;
        } else {
            rear->next = newNode;
            newNode->prev = rear;
            rear = newNode;
        }
        cout << data << " inserted at rear.\n";
    }
    void deleteFront() {
        if (isEmpty()) {
            cout << "Deque is empty. Cannot delete from front.\n";
            return;
        }
        Node* temp = front;
        cout << front->data << " deleted from front.\n";
        front = front->next;
        if (front) front->prev = nullptr;
        else rear = nullptr; // If deque becomes empty
        delete temp;
    }
    void deleteRear() {
        if (isEmpty()) {
            cout << "Deque is empty. Cannot delete from rear.\n";
            return;
        }
        Node* temp = rear;
        cout << rear->data << " deleted from rear.\n";
        rear = rear->prev;
        if (rear) rear->next = nullptr;
        else front = nullptr; // If deque becomes empty
        delete temp;
    }
    int getFront() {
        if (isEmpty()) {
            cout << "Deque is empty.\n";
            return -1;
        }
        return front->data;
    }
    int getRear() {
        if (isEmpty()) {
            cout << "Deque is empty.\n";
            return -1;
        }
        return rear->data;
    }
};
int main() {
    Deque dq;
    dq.insertRear(10);
    dq.insertFront(20);
    cout << "Front element: " << dq.getFront() << "\n";
    cout << "Rear element: " << dq.getRear() << "\n";
    dq.deleteFront();
    dq.deleteRear();
    dq.deleteFront(); // Attempt to delete from empty deque
    return 0;
}
*/

// Task 4:
/*
Palindrome Checker using Queue and Stack
Write a program that checks if a given string is a palindrome. Use a queue and a stack for this purpose.
1.	Enqueue each character of the string into the queue.
2.	Push each character of the string onto the stack.
3.	Dequeue from the queue and pop from the stack simultaneously, comparing the characters.
4.	If all characters match, it's a palindrome; otherwise, it's not.
*/
/*
#include <iostream>
#include <queue>
#include <stack>
#include <string>
using namespace std;
bool isPalindrome(const string& str) {
    queue<char> charQueue;
    stack<char> charStack;
    for (char ch : str) {
        if (isalnum(ch)) { // Consider only alphanumeric characters
            char lowerCh = tolower(ch);
            charQueue.push(lowerCh);
            charStack.push(lowerCh);
        }
    }
    while (!charQueue.empty()) {
        if (charQueue.front() != charStack.top()) {
            return false; // Mismatch found
        }
        charQueue.pop();
        charStack.pop();
    }
    return true; // All characters matched
}
int main() {
    string input;
    cout << "Enter a string to check if it's a palindrome: ";
    getline(cin, input);
    if (isPalindrome(input)) {
        cout << "\"" << input << "\" is a palindrome.\n";
    } else {
        cout << "\"" << input << "\" is not a palindrome.\n";
    }
    return 0;
}
*/