#include <iostream>
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
        std::cout << "4. Exit" << std::endl;
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
            std::cout << "Exiting..." << std::endl;
            break;

        default:
            std::cout << "Invalid choice. Please try again." << std::endl;
            break;
        }

        std::cout << std::endl;
    } while (choice != 4);

    return 0;
}
