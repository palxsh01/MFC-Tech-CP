#include <iostream>
using namespace std;

void input(int arr[], int len) {    //Function to input elements of the list
    for (int i = 0; i < len; i++) {
        cout << "Enter Element " << i + 1 << ": ";
        cin >> arr[i];
    }
}

void insertionSort(int arr[], int len) {    //Sorting algorithm
    for (int i = 1; i < len; i++) {
        int key = arr[i];    //Storing current element to be sorted as key
        int k = i - 1;    
        while (k >= 0 && arr[k] > key) {    //Checking if the element is lesser than key
            arr[k + 1] = arr[k];    //Shifting elements one index to the right
            k--;
        }
        arr[k + 1] = key;    //Once loop breaks, place key in the correct index
    }
}

void display(int arr[], int len) {    //Function to print the list after sorting
    cout << "Sorted List: " << endl;
    for (int i = 0; i < len; i++) {
        cout << arr[i] << " ";
    }
}

int main() {
    int len;    //Variable to store the length of the list
    cout << "Enter length of list: ";
    cin >> len;
    int list[len];    //Declaring an empty list
    input(list, len);    //Taking input
    insertionSort(list, len);    //Sorting list
    display(list, len);    //Displaying sorted list
    return 0;
}
