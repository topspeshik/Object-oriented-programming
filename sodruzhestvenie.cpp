
#include <iostream>
using namespace std;


int div(int numb)
{
    int sum = 0;
    for (int i = 1; i < numb; i++)
    {
        if (numb % i == 0)
        {
           sum += i;
        }
    }
    return sum-1;
}

int main()
{
    
    for (int i = 1; i < 10001; i++)
    {
        int m, n;
        m = div(i);
        n = div(m);
        if (i == n  && i < m)
            cout << i << " " << m << endl;
    }


}
