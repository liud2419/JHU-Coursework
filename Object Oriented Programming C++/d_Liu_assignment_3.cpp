#include <iostream>
#include <string>

// Date class for representing dates
class Date {
public:
    Date() : month(0), day(0), year(0) {}

    Date(int month, int day, int year) : month(month), day(day), year(year) {}

    friend std::ostream& operator<<(std::ostream& os, const Date& date) {
        os << date.month << "/" << date.day << "/" << date.year;
        return os;
    }

private:
    int day;
    int month;
    int year;
};

// Array template class
template <typename T>
class Array {
public:
    Array(int size) : size(size), elements(new T[size]) {}

    ~Array() {
        delete[] elements;
    }

    T& operator[](int index) {
        return elements[index];
    }

private:
    int size;
    T* elements;
};

int main() {
    // Create arrays of integers, floats, strings, and Date objects
    Array<int> intArray(5);
    Array<float> floatArray(3);
    Array<std::string> stringArray(5);
    Array<Date> dateArray(2);

    // Assign values to the arrays
    intArray[0] = 1;
    intArray[1] = 2;
    intArray[2] = 3;
    intArray[3] = 4;
    intArray[4] = 5;

    floatArray[0] = 3.75f;
    floatArray[1] = 8.34f;
    floatArray[2] = 9.99f;

    stringArray[0] = "Hi";
    stringArray[1] = "there,";
    stringArray[2] = "this";
    stringArray[3] = "is";
    stringArray[4] = "David";

    dateArray[0] = Date(8, 8, 2002);
    dateArray[1] = Date(7, 24, 2023);

    // Display the arrays
    std::cout << "Integer Array:" << std::endl;
    for (int i = 0; i < 5; ++i) {
        std::cout << intArray[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "Float Array:" << std::endl;
    for (int i = 0; i < 3; ++i) {
        std::cout << floatArray[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "String Array:" << std::endl;
    for (int i = 0; i < 5; ++i) {
        std::cout << stringArray[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "Date Array:" << std::endl;
    for (int i = 0; i < 2; ++i) {
        std::cout << dateArray[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
