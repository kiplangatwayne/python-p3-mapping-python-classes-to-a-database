# lib/song.py

import sqlite3

class Song:

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        # Establish a connection and create a cursor
        conn = sqlite3.connect("music.db")
        cursor = conn.cursor()

        cursor.execute(sql)
        conn.commit()
        conn.close()

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        # Establish a connection and create a cursor
        conn = sqlite3.connect("music.db")
        cursor = conn.cursor()

        cursor.execute(sql, (self.name, self.album))
        conn.commit()

        self.id = cursor.lastrowid
        conn.close()

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song
