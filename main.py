from musicalbums import MusicAlbums

def main():
    musicalbums = MusicAlbums("musicalbums.db")
    musicalbums.create_db()
    print(get_year_of_birth())
main()