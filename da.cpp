// RestoreName.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>

int main()
{

    std::string name;


    std::ifstream in("C:\\Users\\Gabri\\source\\repos\\SavedName.txt");

    in >> name;

    if (name.size() > 0) {
        std::cout << "Hello " << name << "!\n";
    }
    else {
        std::cout << "No name found!\n";
    }

}