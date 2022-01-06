

#include <iostream>
#include <list>
#include <cmath>
using namespace std;

int main()
{
	int value, mod = 0, sum = 0, count = 0;
	list<int> code;
	cin >> value;

	while (value != 0) {
		mod = value % 3;
		code.push_back(mod);
		code.push_back(mod);
		value = floor(value / 3);


	};
	
	for (auto i = code.begin(); i!=code.end(); ++i)
	{
		sum += (*i * pow(3, count));
		count++;
	}

	cout << sum << endl;
}

