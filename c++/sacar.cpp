#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

int main()
{
    std::vector<std::string> names;
    std::string name;
     while (true) {
        std::cout << "Give me a name (or press Enter to finish): ";
        std::getline(std::cin, name);

        if (name.empty()) {
            break; // Salir del bucle si se ingresa una cadena vacía
        }

        names.push_back(name); // Agregar el nombre al vector
    }

    // Serializar los nombres en un solo string separado por comas
    std::stringstream ss;
    for (size_t i = 0; i < names.size(); ++i) {
        if (i != 0) {
            ss << ","; // Separador entre nombres
        }
        ss << names[i];
    }

    // Guardar los nombres en el archivo
    std::ofstream out("C:\\Users\\Gabri\\source\\repos\\schore.txt");
    if (out.is_open()) {
        out << ss.str();
        out.close();
        std::cout << "Names have been saved to file.\n";
    } else {
        std::cerr << "Unable to open file for writing.\n";
    }

    return 0;
}