
#include <iostream>
#include <stack>
using namespace std;

int main()
{
	const int N = 11;
	int mas[N] = { 12, 5, 3, 2, 45, 96, 6, 8, 11, 24, 11 };

	int i, j;
	int left = 0;
	int right = N-1;

	stack <int> stk;

	stk.push(left);
	stk.push(right);

	do
	{
		right = stk.top();
		stk.pop();
		left = stk.top();
		stk.pop();

		i = left;
		j = right;

		int pivot = (i + j) / 2;
		int pivot_value = mas[pivot];

		do
		{
			while (mas[i] < pivot_value)
				i++;
			while (mas[j] > pivot_value)
				j--;

			if (i <= j)
			{
				int t = mas[i];
				mas[i] = mas[j];
				mas[j] = t;
				i++;
				j--;
			}

		} while (i <= j);

		if (left < j)
		{
			stk.push(left);
			stk.push(j);
		}

		if (i < right)
		{
			stk.push(i);
			stk.push(right);
		}


	} while (!stk.empty());


	for (int i = 0; i < N; i++)
	{
		cout << mas[i] << " ";
	}
}