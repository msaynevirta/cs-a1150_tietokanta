from musicalbums import MusicAlbums

def main():
    musicalbums = MusicAlbums("musicalbums.db")
    musicalbums.create_db()

main()