#include <iostream>

class MyArray {
private:
  int* data;
  int size;

public:
  MyArray(int sz) {
    data = new int[sz];
    size = sz;
  }

  // Copy constructor
  MyArray(const MyArray& other) {
    size = other.size;
    data = new int[size];
    for (int i = 0; i < size; i++) {
      data[i] = other.data[i];
    }
  }

  // Destructor
  ~MyArray() {
    delete[] data;
  }

  // Getter method for size
  int getSize() const {
    return size;
  }

  // Setter method for an element at a specific index
  void setElement(int index, int value) {
    if (index >= 0 && index < size) {
      data[index] = value;
    }
  }

  // Display method to print the elements of the array
  void display() const {
    for (int i = 0; i < size; i++) {
      std::cout << data[i] << " ";
    }
    std::cout << std::endl;
  }
};

int main() {
  // Create an instance of MyArray
  MyArray existingObj(10);

  // Set elements of existingObj
  existingObj.setElement(0, 1);
  existingObj.setElement(1, 2);
  existingObj.setElement(2, 3);
  existingObj.setElement(3, 5);
  existingObj.setElement(4, 7);
  existingObj.setElement(5, 11);
  existingObj.setElement(6, 13);
  existingObj.setElement(7, 17);
  existingObj.setElement(8, 19);
  existingObj.setElement(9, 23);
  // Create a new object using the copy constructor
  MyArray newobj = existingObj;

  // Display the elements of newobj
  std::cout << "Elements of newobj: ";
  newobj.display();

  return 0;
}
