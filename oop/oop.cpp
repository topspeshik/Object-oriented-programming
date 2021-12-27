
#include <iostream>
#include <cmath>

using namespace std;


class Number
{
	int value;


public:


	Number()
	{
		value = 0;
	}

	Number(int valueF)
	{
		this->value = valueF;
	}


	friend Number operator +(const Number& v1, const Number& v2);

	friend Number operator -(const Number& v1, const Number& v2);

	friend Number operator /(const Number& v1, const Number& v2);

	friend Number operator %(const Number& v1, const Number& v2);

	friend Number operator *(const Number& v1, const Number& v2);

	friend Number operator ^(const Number& v1, const Number& v2);

	friend ostream& operator<< (ostream& out, const Number& v);

	void sort(Number *arr, int size)
	{
		Number temp;
		
		for (int i = 0; i < size; i++)
		{
			for (int j = size - 1; j > i; j--)
			if (arr[j].getValue() < arr[j - 1].getValue())
			{
				temp = arr[j];
				arr[j] = arr[j - 1];
				arr[j - 1] = temp;
			}
		}
	}

	int convert_base(int s = 10) 
	{
		if (s == 2) 
		{
			return decToBin(this->value);
		}

		if (s == 8)
		{
			return decToOct(this->value);
		}

		if (s == 16)
		{
			decToHex(this->value);
			return 0;
		}

	}

	int decToBin(int value)
	{
		int c = 0, r = 1;
		
		while (value)
		{
			c += (value % 2) * r;
			value = value / 2;
			r = r * 10;
		}

		return c;
	}

	int decToOct(int value)
	{
		int c = 1;
		int mod = 0;
		int oct = 0;
		while (value) {
			mod = value % 8;
			oct += c * mod;
			value /= 8;
			c *= 10;
		}

		return oct;
	}

	void decToHex(int value)
	{
		int c = 1;
		int d;
		while (c * 16 <= value)
			c *= 16;
		do {
			switch (d = value / c)
			{
			case 0:cout << '0'; break;
			case 1:cout << '1'; break;
			case 2:cout << '2'; break;
			case 3:cout << '3'; break;
			case 4:cout << '4'; break;
			case 5:cout << '5'; break;
			case 6:cout << '6'; break;
			case 7:cout << '7'; break;
			case 8:cout << '8'; break;
			case 9:cout << '9'; break;
			case 10:cout << 'a'; break;
			case 11:cout << 'b'; break;
			case 12:cout << 'c'; break;
			case 13:cout << 'd'; break;
			case 14:cout << 'e'; break;
			case 15:cout << 'f'; break;
			}

			value %= c;
			c /= 16;

		} while (c);
	}

	int getValue() { return this->value; }

};




Number operator+(const Number& v1, const Number& v2)
{
	return Number(v1.value + v2.value);
}

Number operator-(const Number& v1, const Number& v2)
{
	return Number(v1.value - v2.value);
}

Number operator/(const Number& v1, const Number& v2)
{
	return Number(v1.value / v2.value);
}

Number operator%(const Number& v1, const Number& v2)
{
	return Number(v1.value % v2.value);
}

Number operator*(const Number& v1, const Number& v2)
{
	return Number(v1.value * v2.value);
}

Number operator^(const Number& v1, const Number& v2)
{
	return Number(pow(v1.value, v2.value));
}

ostream& operator<<(ostream& os, const Number& v) {
	return os << v.value << endl;
}







int main()
{
	setlocale(LC_ALL, "ru");

	Number a(22);
	Number b(33);
	Number c(3);
	Number d(10);

	cout << a + b << endl;
	cout << "Сложение экземпляра a = 22 и b = 33" << endl;

	Number sum = b + a;
	cout << sum.getValue() << endl;

	cout << "=========================" << endl;

	cout << "Вывод в 16 системе" << endl;
	cout << sum.convert_base(16) << endl;

	cout << "Вывод в 8 системе" << endl;
	cout << sum.convert_base(8) << endl;

	cout << "Вывод в 2 системе" << endl;
	cout << sum.convert_base(2) << endl;

	const int SIZE = 4;
	
	Number arr[SIZE];
	arr[0] = a;
	arr[1] = b;
	arr[2] = c;
	arr[3] = d;

	cout << "=========================" << endl;
	cout << "Вывод массива экземпляров" << endl;

	for (int i = 0; i < SIZE; i++)
	{
		cout << arr[i].getValue() << endl;
	}

	cout << "=========================" << endl;
	cout << "Сортировка массива экземпляров" << endl;

	Number arrSort;
	arrSort.sort(arr, SIZE);
	
	for (int i = 0; i < SIZE; i++)
	{
		cout << arr[i].getValue() << endl;
	}

}

