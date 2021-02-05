
#include <iostream>
using namespace std;


int main()
{
    int pow, a, b, c, d, e, f, a1, b1, c1, d1, e1, f1;

    for (int i = 1; i < 1000000; i++)
    {
        if (i < 10)
            pow = 1;
        else if (i < 100)
            pow = 2;
        else if (i < 1000)
            pow = 3;
        else if (i < 10000)
            pow = 4;
        else if (i < 100000)
            pow = 5;
        else if (i < 1000000)
            pow = 6;

        a1 = 1;
        b1 = 1;
        c1 = 1;
        d1 = 1;
        e1 = 1;
        f1 = 1;

        a = i / 100000;
        b = i / 10000 % 10;
        c = i / 1000 % 10;
        d = i / 100 % 10;
        e = i / 10 % 10;
        f = i % 10;


        cout << a << endl;

        for (int j = 0; j < pow; j++)
        {
            a1 = a1 * a;
            b1 = b1 * b;
            c1 = c1 * c;
            d1 = d1 * d;
            e1 = e1 * e;
            f1 = f1 * f;

        }

        if ((a1 + b1 + c1 + d1 + e1 + f1) == i)
            cout << i << endl;

    }

}
