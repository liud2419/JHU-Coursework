#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

class Song {
private:
    std::string title;
    std::string artistName;
    std::string genre;

public:
    Song(const std::string& title, const std::string& artistName, const std::string& genre)
        : title(title), artistName(artistName), genre(genre) {}

    std::string getTitle() const {
        return title;
    }

    std::string getArtistName() const {
        return artistName;
    }

    std::string getGenre() const {
        return genre;
    }
};

class SongCollection {
private:
    std::vector<Song> songs;

public:
    void addSong(const Song& song) {
        songs.push_back(song);
    }

    void displaySongs() const {
        std::cout << "Songs in the collection:" << std::endl;
        for (const auto& song : songs) {
            std::cout << "Title: " << song.getTitle() << ", Artist: " << song.getArtistName() << ", Genre: " << song.getGenre() << std::endl;
        }
    }

    void displaySortedByArtist() {
        std::vector<Song> sortedSongs = songs;
        std::sort(sortedSongs.begin(), sortedSongs.end(), [](const Song& a, const Song& b) {
            return a.getArtistName() < b.getArtistName();
        });

        std::cout << "Songs in the collection sorted by Artist Name:" << std::endl;
        for (const auto& song : sortedSongs) {
            std::cout << "Title: " << song.getTitle() << ", Artist: " << song.getArtistName() << ", Genre: " << song.getGenre() << std::endl;
        }
    }

    void saveToFile(const std::string& filename) {
        std::ofstream file(filename);
        if (!file.is_open()) {
            std::cerr << "Error: Unable to open the file." << std::endl;
            return;
        }

        for (const auto& song : songs) {
            file << song.getTitle() << "," << song.getArtistName() << "," << song.getGenre() << std::endl;
        }

        file.close();
        std::cout << "Song collection has been saved to the file: " << filename << std::endl;
    }

    void loadFromFile(const std::string& filename) {
        std::ifstream file(filename);
        if (!file.is_open()) {
            std::cerr << "Error: Unable to open the file." << std::endl;
            return;
        }

        songs.clear(); // Clear the current collection before loading from the file

        std::string line;
        while (std::getline(file, line)) {
            std::string title, artist, genre;
            std::size_t pos1 = line.find(',');
            std::size_t pos2 = line.rfind(',');
            if (pos1 != std::string::npos && pos2 != std::string::npos && pos1 != pos2) {
                title = line.substr(0, pos1);
                artist = line.substr(pos1 + 1, pos2 - pos1 - 1);
                genre = line.substr(pos2 + 1);

                songs.push_back(Song(title, artist, genre));
            }
        }

        file.close();
        std::cout << "Song collection has been loaded from the file: " << filename << std::endl;
    }
};

int main() {
    SongCollection collection;

    int choice;
    std::string title, artistName, genre;

    do {
        std::cout << "Options: " << std::endl;
        std::cout << "1. Add a Song to the collection" << std::endl;
        std::cout << "2. Display the Song collection" << std::endl;
        std::cout << "3. Display the collection sorted alphabetically by artist name" << std::endl;
        std::cout << "4. Save the collection to a file" << std::endl;
        std::cout << "5. Load the collection from a file" << std::endl;
        std::cout << "6. Exit" << std::endl;
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
        case 1:
            std::cout << "Enter Song Title: ";
            std::cin.ignore(); // Ignore newline character from the previous input
            std::getline(std::cin, title);
            std::cout << "Enter Artist Name: ";
            std::getline(std::cin, artistName);
            std::cout << "Enter Genre: ";
            std::getline(std::cin, genre);
            collection.addSong(Song(title, artistName, genre));
            break;

        case 2:
            collection.displaySongs();
            break;

        case 3:
            collection.displaySortedByArtist();
            break;

        case 4:
            std::cout << "Enter the filename to save the collection: ";
            std::cin.ignore(); // Ignore newline character from the previous input
            std::getline(std::cin, title);
            collection.saveToFile(title);
            break;

        case 5:
            std::cout << "Enter the filename to load the collection from: ";
            std::cin.ignore(); // Ignore newline character from the previous input
            std::getline(std::cin, title);
            collection.loadFromFile(title);
            break;

        case 6:
            std::cout << "Exiting..." << std::endl;
            break;

        default:
            std::cout << "Invalid choice. Please try again." << std::endl;
            break;
        }

        std::cout << std::endl;
    } while (choice != 6);

    return 0;
}
