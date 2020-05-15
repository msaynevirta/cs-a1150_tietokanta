import csv

from musicalbums import MusicAlbums

def main():
    musicalbums = MusicAlbums("musicalbums.db")
    musicalbums.create_db()
    print(musicalbums.get_year_of_birth())

    filepath = input("Please enter file path for a csv file of new albums: ")

    with(open(filepath, 'r')) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            musicalbums.new_album(row[0], row[1], row[2], row[3], row[4])
main()