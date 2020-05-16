import csv
import os.path
from os import path

from musicalbums import MusicAlbums

def main():
    db_path = "musicalbums.db"
    musicalbums = MusicAlbums(db_path)
    if not path.exists(db_path):
        musicalbums.create_db()

    print("Ed Sheeran's birthyear:", musicalbums.get_year_of_birth())

    filepath = input("Please enter file path for a csv file of new albums: ")

    with(open(filepath, 'r')) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            musicalbums.new_album(row[0], row[1], row[2], row[3], row[4])

    inp = input("Insert company name: ")
    musicalalbums.albums_by_company(inp)
main()