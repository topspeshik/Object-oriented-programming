#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <iomanip>
using namespace std;

int main()
{
    
    setlocale(LC_ALL,"ru");
    string path = "role.txt";

    ifstream fin;
    fin.open(path);
    string str;
    list<string> theatre;
    list<string> roles;
    list<string> textLines;

    while (getline(fin, str))
    {
        theatre.push_back(str);
    }
    
    int index = 0;

    for (auto i = theatre.begin(); i != theatre.end(); i++)
    {
        index++;
        if (*i == "textLines:")
            break;
        roles.push_back(*i);
    }

    roles.pop_front();

    for (int i = 0; i < index; i++)
    {
        theatre.pop_front();
    }
    
    textLines = theatre;
    int count = 1;
    for (auto i = textLines.begin(); i != textLines.end(); i++)
    {
        
        *i = to_string(count) + ")" + *i;
        count++;
    }
    
    multimap<string, string> teatr;
    int foundRole = 0;
    for (auto i = roles.begin(); i != roles.end(); i++)
    {
        string stri;
        stri = *i;
        for (auto j = textLines.begin(); j != textLines.end(); j++)
        {
            string strj;
            strj = *j;
            if (strj.find(stri) != string::npos)
            {
                foundRole = 1;
                strj.replace(2, stri.length()+2, "");
                teatr.emplace(stri, strj);
                *j = "used";
                
            }
            
        }
        if (foundRole == 1) {
            *i = "used";
            foundRole = 0;
        }
    }




    string nothing = "nothing";
    for (const auto& i : teatr)
    {
        if (nothing != i.first)
        {
            cout << i.first << endl;
            nothing = i.first;
        }
        cout << i.second << endl;
    }

    cout << "Слова автора: " << endl;
    for (auto i = textLines.begin(); i != textLines.end(); i++)
    {
        string stri = *i;
        if (stri.find("used") == string::npos)
            cout << *i << endl;
    }

    cout << "Неиспользованные роли: " << endl;
    for (auto i = roles.begin(); i != roles.end(); i++)
    {
        string stri = *i;
        if (stri.find("used") == string::npos)
            cout << *i << endl;
    }

  

}

