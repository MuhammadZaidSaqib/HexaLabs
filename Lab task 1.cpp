// Created by zaids on 9/16/2025.
//

//
// Created by zaids on 9/15/2025.
//

/*1.	Write a c++ program to create a structure name Person with attributes of name (string),
age (integer) and gender (character), take user input for the three fields and display the stored details.*/

/*#include <iostream>
using namespace std;

struct student {
    string name;
    int age;
    string gender;
};

int main() {
    student s;

    cout << "Enter name: ";
    cin >> s.name;

    cout << "Enter age: ";
    cin >> s.age;

    cout << "Enter gender: ";
    cin >> s.gender;

    cout << "\nStudent Details:" << endl;
    cout << "Name: " << s.name << endl;
    cout << "Age: " << s.age << endl;
    cout << "Gender: " << s.gender << endl;

    return 0;
}*/



/*Q2.	Implement a structure Rectangle with attributes of length and width,
Prompt to take the values form the users and calculate and print the area.*/

/*#include<iostream>
using namespace std;
struct Rectangle {
    float length;
    float width;
};
int main() {
    Rectangle rect;

    cout << "Enter length of the rectangle: ";
    cin >> rect.length;

    cout << "Enter width of the rectangle: ";
    cin >> rect.width;

    float area = rect.length * rect.width;

    cout << "Area of the rectangle: " << area << endl;

    return 0;
}*/


/*
3	Create a simple hospital patient record system using C++ structures. The program will be able to:
•	Store 5 patient's details (ID, Name, Age).
•	Use functions to add and display patient records.  */


/*#include <iostream>
using namespace std;

struct Patient {
    int id;
    string name;
    int age;
};

void addPatients(Patient patients[], int size) {
    for (int i = 0; i < size; i++) {
        cout << "Enter details for patient " << i + 1 << ":\n";
        cout << "ID: ";
        cin >> patients[i].id;
        cout << "Name: ";
        cin >> patients[i].name;
        cout << "Age: ";
        cin >> patients[i].age;
    }
}

void displayPatients(const Patient patients[], int size) {
    cout << "\nPatient Records:\n";
    for (int i = 0; i < size; ++i) {
        cout << "ID: " << patients[i].id
             << ", Name: " << patients[i].name
             << ", Age: " << patients[i].age << endl;
    }
}

int main() {
    const int NUM_PATIENTS = 5;
    Patient patients[NUM_PATIENTS];

    addPatients(patients, NUM_PATIENTS);
    displayPatients(patients, NUM_PATIENTS);

    return 0;
}*/
