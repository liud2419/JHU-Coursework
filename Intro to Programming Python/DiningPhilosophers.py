import time
from fork import Fork
from philosopher import Philosopher

def DiningPhilosophers():
    # create array of 5 names: Plato, Aristotle, Buddha, Marx, and Nietzsche
    names = ["Plato", "Aristotle", "Buddha", "Marx", "Nietzsche"]

    # create five forks and append them to a list
    forks = []
    for i in range(5):
        fork = Fork()
        forks.append(fork)

    # create a list of five philosophers and assign the appropriate forks to each
    philosophers = []
    for i in range(5):
        # get the index of the next fork in the list
        next_fork_index = i + 1 if i + 1 < 5 else 0
        philosopher = Philosopher(names[i], forks[i], forks[next_fork_index])
        philosophers.append(philosopher)

    # start all 5 Philosopher threads (should be non-blocking)
    for philosopher in philosophers:
        philosopher.start()

    # sleep for 10 seconds
    time.sleep(10)

    # set ‘running’ to False
    Philosopher.running = False

    # exit all threads
    for philosopher in philosophers:
        philosopher.join()

if __name__ == "__main__":
    DiningPhilosophers()