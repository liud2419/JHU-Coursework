#include <iostream>
#include <vector>

using namespace std;

// Class representing a soft drink
class SoftDrink {
private:
    string name;
    double price;

public:
    SoftDrink(const string& name, double price) : name(name), price(price) {}

    string getName() const {
        return name;
    }

    double getPrice() const {
        return price;
    }
};

// Class representing a vending machine
class VendingMachine {
private:
    vector<SoftDrink> drinks;
    double balance;

public:
    VendingMachine() : balance(0.0) {}

    void addDrink(const SoftDrink& drink) {
        drinks.push_back(drink);
    }

    void displayOptions() const {
        cout << "Available drinks:\n";
        for (size_t i = 0; i < drinks.size(); ++i) {
            cout << i + 1 << ". " << drinks[i].getName() << " ($" << drinks[i].getPrice() << ")\n";
        }
    }

    void insertMoney() {
        double amount;
        cout << "Enter amount to insert: $";
        cin >> amount;
        balance += amount;
    }

    void dispenseDrink() {
        int selection;
        cout << "Enter your selection: ";
        cin >> selection;

        if (selection >= 1 && selection <= static_cast<int>(drinks.size())) {
            const SoftDrink& selectedDrink = drinks[selection - 1];
            if (balance >= selectedDrink.getPrice()) {
                cout << "Dispensing " << selectedDrink.getName() << ". Enjoy!\n";
                balance -= selectedDrink.getPrice();
            } else {
                cout << "Insufficient funds. Current balance is: " << balance << " Please insert more money.\n";
                insertMoney(); // Prompt user to insert more money
                dispenseDrink(); // Retry dispensing the drink
                return;
            }
        } else {
            cout << "Invalid selection. Please try again.\n";
        }
    }

    void returnChange() {
        if (balance > 0) {
            cout << "Returning change: $" << balance << endl;
            balance = 0.0;
        }
    }
};

int main() {
    // Create a vending machine object
    VendingMachine machine;

    // Add some soft drinks to the machine
    machine.addDrink(SoftDrink("Coke", 1.25));
    machine.addDrink(SoftDrink("Mexican Coke", 1.50));
    machine.addDrink(SoftDrink("Japanese Coke", 1.75));
    machine.addDrink(SoftDrink("Water", 1.00));

    // Display the available options
    machine.displayOptions();

    // Insert money
    machine.insertMoney();

    // Select a drink and dispense
    machine.dispenseDrink();

    // Return change, if any
    machine.returnChange();

    return 0;
}
