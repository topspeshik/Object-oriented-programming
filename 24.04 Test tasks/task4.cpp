﻿

#include <iostream>

using namespace std;

int check(int a[5], int arr[10][10]) {
    int temp = 0;
    for (int i = 0; i < 5; i++)
    {
        temp = arr[temp][a[i]];
    }

    return temp;
}



int main()
{
    const int rows = 10;
    const int cols = 10;

    int arr[rows][cols] = {
        {0, 3, 1, 7, 5, 9, 8, 6, 4, 2},
        {7, 0, 9, 2, 1, 5, 4, 8, 6, 3},
        {4, 2, 0, 6, 8, 7, 1, 3, 5, 9},
        {1, 7, 5, 0, 9, 8, 3, 4, 2, 6},
        {6, 1, 2, 3, 0, 4, 5, 9, 7, 8},
        {3, 6, 7, 4, 2, 0, 9, 5, 8, 1},
        {5, 8, 6, 9, 7, 2, 0, 1, 3, 4},
        {8, 9, 4, 5, 3, 6, 2, 0, 1, 7},
        {9, 4, 3, 8, 6, 1, 7, 2, 0, 5},
        {2, 5, 8, 1, 4, 3, 6, 7, 9, 0}
    };

    /*for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            cout << arr[i][j] << "\t";
        }
        cout << endl;
    }
    */

    int numb;
    cin >> numb;

    int n1, n2, n3, n4, n5;
    n5 = numb % 10;
    n4 = numb % 100 / 10;
    n3 = numb % 1000 / 100;
    n2 = numb % 10000 / 1000;
    n1 = numb % 100000 / 10000;

    
    int a[5] = { n1, n2 ,n3 ,n4 ,n5 };

    
    int temp1;
    temp1 = check(a, arr);

    if (temp1 != 0) {
        for (int i = 0; i < 4; i++)
        {
            int time;
            time = a[i];
            a[i] = a[i+1];
            a[i + 1] = time;
            int temp = check(a, arr);
            if (temp == 0) {
                break;
            }
            else {
                time = a[i + 1];
                a[i + 1] = a[i];
                a[i] = time;
            }
        }
    }

    cout << temp1 << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << a[i];
    }

}

