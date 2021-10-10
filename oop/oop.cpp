
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
		value = valueF;
	}

	

	friend Number operator +(const Number& v1, const Number& v2);
	
	friend Number operator -(const Number& v1, const Number& v2);

	friend Number operator /(const Number& v1, const Number& v2);

	friend Number operator %(const Number& v1, const Number& v2);

	friend Number operator *(const Number& v1, const Number& v2);

	friend Number operator ^(const Number& v1, const Number& v2);

	int getValue() { return value; }
	
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
	return Number(pow(v1.value,v2.value));
}




int main()
{
	Number a(2);
	Number b(3);

	Number c =  b+a;
	cout <<  c.getValue();

}
