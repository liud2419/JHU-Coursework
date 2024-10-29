#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

// Function to display the current list of movies
void displayMovies(const list<string>& movies) {
    if (movies.empty()) {
        cout << "No movies in the list.\n";
    } else {
        cout << "Top 5 Movies:\n";
        int rank = 1;
        for (const auto& movie : movies) {
            cout << rank << ". " << movie << endl;
            rank++;
        }
    }
}

// Function to change the ranking of a movie
void changeRanking(list<string>& movies) {
    displayMovies(movies);
    int current_rank, new_rank;

    cout << "Enter the current ranking of the movie you want to change: ";
    cin >> current_rank;

    if (current_rank < 1 || current_rank > 5) {
        cout << "Invalid ranking. Please enter a ranking between 1 and 5.\n";
        return;
    }

    cout << "Enter the new ranking for the movie: ";
    cin >> new_rank;

    if (new_rank < 1 || new_rank > 5) {
        cout << "Invalid ranking. Please enter a ranking between 1 and 5.\n";
        return;
    }

    if (current_rank == new_rank) {
        cout << "The movie is already ranked at position " << new_rank << ".\n";
        return;
    }

    // Find the movie at the current rank and move it to the new rank
    auto it = movies.begin();
    advance(it, current_rank - 1);

    string movie = *it;
    movies.erase(it);

    it = movies.begin();
    advance(it, new_rank - 1);

    movies.insert(it, movie);
}

int main() {
    list<string> movies;
    int choice;

    do {
        cout << "Menu:\n";
        cout << "1. Enter a new movie list\n";
        cout << "2. Display the current list of movies\n";
        cout << "3. Change the ranking of a movie\n";
        cout << "4. Quit the program\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                movies.clear();
                cout << "Enter your top 5 movie choices:\n";
                cin.ignore();
                for (int i = 0; i < 5; ++i) {
                    string movie;
                    cout << "Movie #" << (i + 1) << ": ";
                    getline(cin, movie);
                    movies.push_back(movie);
                }
                break;
            }
            case 2:
                displayMovies(movies);
                break;
            case 3:
                changeRanking(movies);
                break;
            case 4:
                cout << "Exiting the program.\n";
                break;
            default:
                cout << "Invalid choice. Please enter a valid option.\n";
        }
    } while (choice != 4);

    return 0;
}
