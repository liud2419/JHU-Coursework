#include <iostream>

class Counter {
private:
    int value;

public:
    Counter() : value(0) {}

    void increment() {
        value++;
    }

    void decrement() {
        value--;
    }

    void reset() {
        value = 0;
    }

    int getValue() const {
        return value;
    }
};

class MemoryCounter {
private:
    Counter counter;
    int memory;

public:
    MemoryCounter() : memory(0) {}

    void resetMemory() {
        memory = 0;
    }

    void addMemory() {
        memory += counter.getValue();
    }

    void incrementCounter() {
        counter.increment();
    }

    void decrementCounter() {
        counter.decrement();
    }

    void resetCounter() {
        counter.reset();
    }

    void displayValues() const {
        std::cout << "Current Value: " << counter.getValue() << std::endl;
        std::cout << "Memory Value: " << memory << std::endl;
    }
};

int main() {
    MemoryCounter memoryCounter;
    memoryCounter.incrementCounter();
    memoryCounter.displayValues();
    memoryCounter.addMemory();
    memoryCounter.incrementCounter();
    memoryCounter.displayValues();
    memoryCounter.resetMemory();
    memoryCounter.displayValues();

    return 0;
}
