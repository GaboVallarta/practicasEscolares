#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

int main() {
    std::ifstream in("C:\\Users\\Gabri\\source\\repos\\schore.txt");

    if (!in.is_open()) {
        std::cerr << "Unable to open file for reading.\n";
        return 1;
    }

    std::string line;
    std::getline(in, line);

    std::vector<std::string> names;
    std::stringstream ss(line);
    std::string name;
    
    // Leer nombres separados por comas y almacenarlos en el vector
    while (std::getline(ss, name, ',')) {
        names.push_back(name);
    }

    if (!names.empty()) {
        std::cout << "Hello ";
        for (const std::string& n : names) {
            std::cout << n << ", ";
        }
        std::cout << "!\n";
    } else {
        std::cout << "No names found!\n";
    }

    return 0;
}