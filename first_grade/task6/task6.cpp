// z6.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;

int main()
{

    setlocale(LC_ALL, "RU");

    int rows;
    int cols;
    int i, j;
    int index = 0;
    int max = 0;
    int sum = 0;
    int** arr;
    cin >> rows;
    cin >> cols;

    arr = new int* [rows];
    for (i = 0; i < rows; i++)
        arr[i] = new int[cols];


    

    for (int i = 0; i < rows; i++)
    {
        cout << "Номер столбца " << i << endl << "Введите строку  " << endl;
        for (int j = 0; j < cols; j++)
        {
           
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            cout << arr[i][j] << "\t";
        }
        cout << endl;
    }

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            sum += arr[i][j];
            
           
        }
        if (sum > max) {
            max = sum;
            index = i;
        }
            
        sum = 0;
    }

    cout << "Максимальная сумма чисел в строке:" << max <<" Номер строки:"<< index<<endl;


}
