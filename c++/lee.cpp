// SaveName.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>


int main()
{
    std::string name;
    std::cout << "Give me your name: ";
    std::cin >> name;

    if (name.size() > 0) {
        std::ofstream out("C:\\Users\\Gabri\\source\\repos\\SavedName.txt");

        out << name;

        out.close();
    }
}