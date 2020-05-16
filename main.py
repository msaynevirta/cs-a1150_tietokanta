import csv

from musicalbums import MusicAlbums

def main():
    db_path = "musicalbums.db"
    musicalbums = MusicAlbums(db_path)

    # ----------- INITIALISE DATABASE -----------
    musicalbums.create_db()

    # ----------- PRINT BIRTHYEAR OF A SINGLE ARTIST -----------
    print("Ed Sheeran's birthyear:", musicalbums.get_year_of_birth())

    # ----------- LOAD AND INSERT COMPANIES FROM EXAMPLE FILE -----------
    with(open("example_companies.csv", 'r')) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            musicalbums.new_company(row[0], row[1], row[2])

    # ----------- LOAD AND INSERT ALBUMS FROM EXAMPLE FILE -----------
    with(open("example_albums.csv", 'r')) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            musicalbums.new_album(row[0], row[1], row[2], row[3], row[4])

    # ----------- LOAD ALBUMS BY COMPANY -----------
    company_name = input("Enter company name: ")

    for row in musicalbums.get_albums_by_company(company_name):
        print(row)
main()