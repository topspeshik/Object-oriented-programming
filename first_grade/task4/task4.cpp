
#include <iostream>
#include <cctype>
#include <string>
using namespace std;

int main()
{
    string stroka;
    getline(cin, stroka);
    for (int i = 0; i < stroka.length(); i++) {
        if (stroka[i] == ' ') {
            stroka.erase(i, 1);
            i--;
        }
    }
    double s = 0;
    for (int i = 0; i < stroka.length(); i++)
    {
        if (stroka[i] == 'c' || (stroka[i] == 'g') || (stroka[i] == 'C') || (stroka[i] == 'G'))
        {
            s++;
        }
    }

    cout << s / stroka.length() * 100 << endl;
}

