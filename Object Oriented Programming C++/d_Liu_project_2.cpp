#include <iostream>
#include <queue>
#include <random>
#include <vector>

using namespace std;

class Passenger {
private:
    int id;
    int arrivalTime;
    int queueEntryTime;
    int validationTime;
    int scanStartTime;
    int totalWaitTime;

public:
    Passenger(int _id, int _arrivalTime) : id(_id), arrivalTime(_arrivalTime),
                                           queueEntryTime(0), validationTime(0),
                                           scanStartTime(0), totalWaitTime(0) {}

    int getID() const { return id; }
    int getArrivalTime() const { return arrivalTime; }
    int getQueueEntryTime() const { return queueEntryTime; }
    int getValidationTime() const { return validationTime; }
    int getScanStartTime() const { return scanStartTime; }
    int getTotalWaitTime() const { return totalWaitTime; }

    void setQueueEntryTime(int time) { queueEntryTime = time; }
    void setValidationTime(int time) { validationTime = time; }
    void setScanStartTime(int time) { scanStartTime = time; }

    void calculateTotalWaitTime() { totalWaitTime = validationTime + (scanStartTime - queueEntryTime); }
};

class PassengerQueue {
private:
    queue<Passenger*> passengers;

public:
    void enqueue(Passenger* passenger) { passengers.push(passenger); }
    void dequeue() { passengers.pop(); }
    bool isEmpty() const { return passengers.empty(); }
    Passenger* front() { return passengers.front(); }
};

class AirportSecuritySimulation {
private:
    vector<PassengerQueue> credentialValidationQueues;
    vector<PassengerQueue> scanningQueues;
    vector<int> credentialValidationTimes;
    vector<int> scanningTimes;
    int totalPassengersServed;
    int totalPassengersWaitTime;
    int totalPassengersInSystem;
    int totalPassengersInQueue;

    int generateRandomExponential(double rate) {
        random_device rd;
        default_random_engine generator(rd());
        exponential_distribution<double> distribution(1.0 / rate);
        return static_cast<int>(distribution(generator));
    }

    void processCredentialValidation(int currentTime) {
        for (int i = 0; i < credentialValidationQueues.size(); i++) {
            if (!credentialValidationQueues[i].isEmpty()) {
                Passenger* passenger = credentialValidationQueues[i].front();
                int validationTime = generateRandomExponential(1.0 / 30); // Average validation time is 30 seconds
                passenger->setValidationTime(currentTime + validationTime);
                passenger->calculateTotalWaitTime();
                totalPassengersWaitTime += passenger->getTotalWaitTime();
                totalPassengersInQueue += currentTime - passenger->getQueueEntryTime();
                credentialValidationTimes.push_back(validationTime);
                credentialValidationQueues[i].dequeue();
                totalPassengersServed++;
            }
        }
    }

    void processScanning(int currentTime) {
        for (int i = 0; i < scanningQueues.size(); i++) {
            if (!scanningQueues[i].isEmpty()) {
                Passenger* passenger = scanningQueues[i].front();
                int scanningTime = generateRandomExponential(1.0 / 150); // Average scanning time is 150 seconds (2.5 minutes)
                passenger->setScanStartTime(currentTime + scanningTime);
                passenger->calculateTotalWaitTime();
                totalPassengersWaitTime += passenger->getTotalWaitTime();
                totalPassengersInQueue += currentTime - passenger->getQueueEntryTime();
                scanningTimes.push_back(scanningTime);
                scanningQueues[i].dequeue();
                totalPassengersServed++;
            }
        }
    }

public:
    AirportSecuritySimulation() : totalPassengersServed(0), totalPassengersWaitTime(0),
                                  totalPassengersInSystem(0), totalPassengersInQueue(0) {}

    void runSimulation() {
        int operatingHours = 20; // Operating hours per day
        int operatingTime = operatingHours * 3600; // Convert to seconds
        int totalTime = 5 * operatingTime; // 5 days of simulation

        int passengerID = 1;
        int currentTime = 0;

        while (currentTime < totalTime) {
            int interarrivalTime = generateRandomExponential(90.0 / 3600); // 90 passengers per hour
            currentTime += interarrivalTime;

            if (currentTime > totalTime)
                break;

            Passenger* newPassenger = new Passenger(passengerID, currentTime);
            passengerID++;

            int minQueueLength = credentialValidationQueues[0].isEmpty() ? 0 : credentialValidationQueues[0].front()->getValidationTime() + currentTime - credentialValidationQueues[0].front()->getQueueEntryTime();
            int minQueueIndex = 0;

            for (int i = 1; i < credentialValidationQueues.size(); i++) {
                if (!credentialValidationQueues[i].isEmpty()) {
                    int queueTime = credentialValidationQueues[i].front()->getValidationTime() + currentTime - credentialValidationQueues[i].front()->getQueueEntryTime();
                    if (queueTime < minQueueLength) {
                        minQueueLength = queueTime;
                        minQueueIndex = i;
                    }
                }
            }

            newPassenger->setQueueEntryTime(currentTime);
            credentialValidationQueues[minQueueIndex].enqueue(newPassenger);
        }

        while (currentTime <= totalTime) {
            processCredentialValidation(currentTime);
            processScanning(currentTime);
            currentTime++;
        }
        
        // Deallocate memory for Passenger objects
        for (int i = 0; i < credentialValidationQueues.size(); i++) {
            while (!credentialValidationQueues[i].isEmpty()) {
                Passenger* passenger = credentialValidationQueues[i].front();
                delete passenger;
                credentialValidationQueues[i].dequeue();
            }
        }

        for (int i = 0; i < scanningQueues.size(); i++) {
            while (!scanningQueues[i].isEmpty()) {
                Passenger* passenger = scanningQueues[i].front();
                delete passenger;
                scanningQueues[i].dequeue();
            }
        }

        int totalDays = totalTime / operatingTime;
        int averagePassengersPerDay = totalPassengersServed / totalDays;
        int averageTotalTimeInSystem = totalPassengersInSystem / totalPassengersServed;
        int averagePassengerWaitTime = totalPassengersWaitTime / totalPassengersServed;

        // Calculate additional metrics
        int averageTimeStageOne = 0;
        int averageWaitTimeStageOne = 0;
        int averageTimeStageTwo = 0;
        int averageWaitTimeStageTwo = 0;

        for (int i = 0; i < credentialValidationTimes.size(); i++) {
            averageTimeStageOne += credentialValidationTimes[i];
            averageWaitTimeStageOne += credentialValidationTimes[i] - credentialValidationQueues[i].front()->getArrivalTime();
        }

        for (int i = 0; i < scanningTimes.size(); i++) {
            averageTimeStageTwo += scanningTimes[i];
            averageWaitTimeStageTwo += scanningTimes[i] - scanningQueues[i].front()->getValidationTime();
        }

        averageTimeStageOne /= totalPassengersServed;
        averageWaitTimeStageOne /= totalPassengersServed;
        averageTimeStageTwo /= totalPassengersServed;
        averageWaitTimeStageTwo /= totalPassengersServed;

        cout << "Total passengers served: " << totalPassengersServed << endl;
        cout << "Average passengers served per day: " << averagePassengersPerDay << endl;
        cout << "Average total time in the system for a customer (seconds): " << averageTotalTimeInSystem << endl;
        cout << "Average passenger total wait time in the system (seconds): " << averagePassengerWaitTime << endl;
        cout << "Average passenger time in stage one (credential validation) process: " << averageTimeStageOne << endl;
        cout << "Average passenger wait time in stage one (credential validation) process: " << averageWaitTimeStageOne << endl;
        cout << "Average passenger time in stage two (scanning) process: " << averageTimeStageTwo << endl;
        cout << "Average passenger wait time in stage two (scanning) process: " << averageWaitTimeStageTwo << endl;
    }

    void addCredentialValidationQueue(int numQueues) {
        credentialValidationQueues.resize(numQueues);
    }

    void addScanningQueue(int numQueues) {
        scanningQueues.resize(numQueues);
    }
};

int main() {
    AirportSecuritySimulation simulation;
    simulation.addCredentialValidationQueue(1); // Add 1 credential validation queue
    simulation.addScanningQueue(4); // Add 4 scanning queues
    simulation.runSimulation();

    return 0;
}
