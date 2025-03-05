#include <iostream>
using namespace std;

void input(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        cout << "Enter Element " << i + 1 << ": ";
        cin >> arr[i];
    }
}

void insertionSort(int arr[], int len) {
    for (int i = 1; i < len; i++) {
        int key = arr[i];
        int k = i - 1;
        while (k >= 0 && arr[k] > key) {
            arr[k + 1] = arr[k];
            k--;
        }
        arr[k + 1] = key;
    }
}

void display(int arr[], int len) {
    cout << "Sorted List: " << endl;
    for (int i = 0; i < len; i++) {
        cout << arr[i] << " ";
    }
}

int main() {
    int len;
    cout << "Enter length of list: ";
    cin >> len;
    int list[len];
    input(list, len);
    insertionSort(list, len);
    display(list, len);
    return 0;
}