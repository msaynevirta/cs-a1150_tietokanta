import sqlite3

class MusicAlbums:
    def __init__(self, filepath):
        self.db = sqlite3.connect(filepath)
        self.cursor = self.db.cursor()

    def create_db(self):
        self.cursor.execute("""
            CREATE TABLE Companies(
                companyName TEXT PRIMARY KEY,
                country TEXT DEFAULT ’USA’,
                webpage TEXT NOT NULL
            );
            CREATE TABLE Albums(
                albumName TEXT,
                companyName TEXT REFERENCES Companies(companyName),
                year INTEGER,
                length INTEGER,
                genre TEXT CHECK (genre IN (’pop’, ’rock’, ’jazz’, ’classical’, ’folk’)),
                PRIMARY KEY (albumName, companyName)
            );
            CREATE TABLE Artists(
                artistName TEXT PRIMARY KEY,
                gender TEXT CHECK (gender IN (’M’, ’F’, ’O’)),
                born INTEGER
            );
            CREATE TABLE Tracks(
                trackNo INTEGER CHECK (trackNo > 0 AND trackNo < 100) NOT NULL,
                albumName TEXT NOT NULL,
                companyName TEXT NOT NULL,
                trackName TEXT,
                artistName TEXT REFERENCES Artists(artistName) NOT NULL,
                composer TEXT,
                lyricist TEXT,
                length INTEGER,
                FOREIGN KEY (albumName, companyName) REFERENCES Albums(albumName, companyName)
            );
            INSERT INTO Artists VALUES('Ed Sheeran', 'M', 1991);
            """)

    def get_year_of_birth(self):
        self.cursor("""SELECT born FROM Artists WHERE artistName = 'Ed Sheeran';""")
        return
