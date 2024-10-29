#include <iostream>
#include <set>
#include <string>

class State {
public:
    State(const std::string& name, const std::string& capital)
        : stateName(name), capitalCity(capital) {}

    // Getter methods
    std::string getStateName() const {
        return stateName;
    }

    std::string getCapitalCity() const {
        return capitalCity;
    }

private:
    std::string stateName;
    std::string capitalCity;
};

// Comparator function for the set to compare State objects based on their names
struct StateComparator {
    bool operator()(const State& state1, const State& state2) const {
        return state1.getStateName() < state2.getStateName();
    }
};

int main() {
    std::set<State, StateComparator> stateSet;

    // Adding State objects to the set directly
    stateSet.insert(State("Illinois", "Springfield"));
    stateSet.insert(State("Wisconsin", "Madison"));
    stateSet.insert(State("California", "Sacramento"));
    stateSet.insert(State("New York", "Albany"));
    stateSet.insert(State("Alaska", "Juneau"));

    // Displaying each state and its capital city
    for (const auto& state : stateSet) {
        std::cout << "State Name: " << state.getStateName()
                  << ", Capital City: " << state.getCapitalCity() << std::endl;
    }

    return 0;
}
