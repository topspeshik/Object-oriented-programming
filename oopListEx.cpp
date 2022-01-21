#include <iostream>
using namespace std;


template<typename T1>
class List
{
public:
	List()
	{
		length = 0;
		frst = nullptr;
	}

	void push_back(T1 data)
	{
		if (frst == nullptr)
		{
			frst = new Node<T1>(data);
		}
		else
		{
			Node<T1>* cur = this->frst;

			while (cur->next != nullptr)
			{
				cur = cur->next;
			}
			cur->next = new Node<T1>(data);

		}

		length++;
	};



	T1& operator[](const int index)
	{
		int counter = 0;

		Node<T1>* cur = this->frst;


		while (cur != nullptr)
		{
			if (counter == index)
			{
				return cur->data;
			}


			cur = cur->next;
			counter++;
		}
	};



	void pop_back()
	{
		if ((length - 1) == 0)
		{
			Node<T1>* temp = frst;

			frst = frst->next;

			delete temp;

			length--;
		}
		else
		{
			Node<T1>* previous = this->frst;
			for (int i = 0; i < length - 2; i++)
			{
				previous = previous->next;
			}


			Node<T1>* toDelete = previous->next;

			previous->next = toDelete->next;

			delete toDelete;

			length--;
		}
	};


	void sort()
	{

		int* arr = new int[length];

		int counter = 0;

		Node<T1>* cur = this->frst;


		while (cur != nullptr)
		{
			if (counter != length)
			{
				arr[counter] = cur->data;
			}
			cur = cur->next;
			counter++;
		}

		Bubble(arr);
		counter = 0;
		cur = this->frst;
		while (cur != nullptr)
		{
			if (counter != length)
			{
				cur->data = arr[counter];
			}
			cur = cur->next;
			counter++;
		}
	}

	int Unique()
	{
		int* arr = new int[length];

		int counter = 0;

		Node<T1>* cur = this->frst;


		while (cur != nullptr)
		{
			if (counter != length)
			{
				arr[counter] = cur->data;
			}
			cur = cur->next;
			counter++;
		}

		counter = 0;

		for (int i = 0; i < length-1; i++)
		{
			for (int  j = i+1; j < length; j++)
			{

				if (arr[i] == arr[j]) {
					counter++;
					break;
				}
			}
		}

		return (length - counter);
	}



	void Merge(int arr[], int begin, int end)
	{
		const int nmax = 1000;
		int i = begin,
			t = 0,
			mid = begin + (end - begin) / 2,
			j = mid + 1,
			d[nmax];

		while (i <= mid && j <= end) {

			if (arr[i] <= arr[j]) {
				d[t] = arr[i]; i++;
			}
			else {
				d[t] = arr[j]; j++;
			}
			t++;
		}

		while (i <= mid) {
			d[t] = arr[i]; i++; t++;

		}

		while (j <= end) {
			d[t] = arr[j]; j++; t++;
		}

		for (i = 0; i < t; i++)
			arr[begin + i] = d[i];
	}

	void Bubble(int* arr)
	{
		int temp;

		for (int j = 0; j < length - 1; j++)
		{
			for (int i = 0; i < length - 1 - j; i++)
			{
				if (arr[i] > arr[i + 1])
				{
					temp = arr[i];
					arr[i] = arr[i + 1];
					arr[i + 1] = temp;
				}
			}
		}

		

	}

	int Find(int value)
	{

		Node<T1>* cur = this->frst;
		int count = 0;
		while (cur->data != value)
		{
			if (cur->next == nullptr) {
				cout << "Элемент не найден" << endl;
				return -1;
			}
			cur = cur->next;
			count += 1;
		}
		return count;
	}

	void reverse()
	{
		Node<T1>* prev = nullptr;
		Node<T1>* next;
		Node<T1>* cur = frst;
		while (cur != nullptr)
		{
			next = cur->next;
			cur->next = prev;
			prev = cur;
			cur = next;
		}
		frst = prev;
	}

	void clear()
	{
		while (length)
		{
			Node<T1>* temp = frst;

			frst = frst->next;

			delete temp;

			length--;
		}
	};

	int getLength()
	{
		return length;
	}

	~List()
	{
		clear();
	}

private:


	template<typename T>
	class Node
	{
	public:

		Node* next;
		T data;

		Node(T data, Node* next = nullptr)
		{
			this->data = data;
			this->next = next;
		}
	};
	int length;
	Node<T1>* frst;
};






int main()
{

	setlocale(LC_ALL, "ru");


	List<int> listik;
	listik.push_back(5);
	listik.push_back(4);
	listik.push_back(15);
	listik.push_back(6);
	listik.push_back(2);
	
	/*cout << "Длина листа: " << listik.getLength() << endl;
	cout << "=====================" << endl;
	for (int i = 0; i < listik.getLength(); i++)
	{
		cout << listik[i] << endl;
	}
	cout << "=====================" << endl;
	cout << "Pop back " << endl;
	listik.pop_back();
	cout << "=====================" << endl;
	for (int i = 0; i < listik.getLength(); i++)
	{
		cout << listik[i] << endl;
	}

	cout << "=====================" << endl;
	listik.reverse();
	cout << "Reverse" << endl;
	cout << "=====================" << endl;
	for (int i = 0; i < listik.getLength(); i++)
	{
		cout << listik[i] << endl;
	}
	cout << "=====================" << endl;
	cout << "push_back(20)" << endl;
	listik.push_back(20);
	cout << "=====================" << endl;
	for (int i = 0; i < listik.getLength(); i++)
	{
		cout << listik[i] << endl;
	}
	cout << "=====================" << endl;
	cout << "Сортировка" << endl;
	listik.sort();
	for (int i = 0; i < listik.getLength(); i++)
	{
		cout << listik[i] << endl;
	}*/

	cout << "Сортировка" << endl;
	listik.sort();
	for (int i = 0; i < listik.getLength(); i++)
	{
		cout << listik[i] << endl;
	}

	listik.push_back(15);
	listik.push_back(15);
	listik.push_back(5);
	cout << "=================" << endl;
	cout << "Unique" << endl;
	cout << listik.Unique() << endl;

	


	return 0;
}