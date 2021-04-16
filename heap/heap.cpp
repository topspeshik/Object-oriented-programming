
#include <iostream>
using namespace std;


class Heapster {
public:
	int length = 0;
	int* storage = new int[length];
	int size = 0;
	
	void insert (int el) {
		storage[size] = el;
		size++;
		
	}

	void heapSort() {
		for (int start = length; start > -1 ; start--)
		{
			heapPick(start, length - 1);
		}

		for (int end = length - 1; end > 0; end--)
		{
			int time = storage[end];
			storage[end] = storage[0];
			storage[0] = time;
			heapPick(0, end - 1);
		}

		
	}

	void heapPick(int start, int end) {
		int index = start;
		int child = 0;
		while (1) {
			child = index * 2 + 1;

			if (child > end) {
				break;
			}

			if ((child + 1 <= end) && (storage[child] < storage[child + 1])) {
				child += 1;
			}

			if (storage[index] < storage[child]) {
				int time = storage[index];
				storage[index] = storage[child];
				storage[child] = time;
				index = child;
			}
			else
				break;
		}
	}

	bool Full() {
		for (int i = 0; i <= length; i++) {
			int lChild = 2 * i + 1;
			int rChild = 2 * i + 2;

			if (((rChild < length) && (lChild >= length)) || ((lChild < length) && (rChild >= length))) {
				return false;
			}
		}
		return true;
	}

};


int main()
{
	setlocale(LC_ALL, "RU");
	int length;
	cout << "Введите кол-во элементов" << endl;
	cin >> length;
	Heapster hs;
	hs.length = length;
	for (int i = 0; i < length; i++)
	{
		int el;
		cin >> el;
		hs.insert(el);
	}

	hs.heapSort();
	
	for (int i = 0; i < length; i++)
	{
		cout << hs.storage[i] << " ";
	}
	cout << endl;
	cout <<"Дерево полное - " << hs.Full() << endl;
	
}

