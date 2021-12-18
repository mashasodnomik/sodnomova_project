import sqlite3
import os

songs = os.listdir(r"C:/Users/USER/PycharmProjects/project/wvwsongs")
for song in songs:
    print(song)

with open("playlist.txt", "r") as f:
    lst = list(f.readlines())
print(lst[0])

for song in songs:
    connection = sqlite3.connect("projectmusic.db")
    cursor = connection.cursor()
    with open(f"{song}", "rb") as bin_wav:
        b = bin_wav.read()
        query = """INSERT INTO TRACK (bytes) VALUES (?)"""
        result = cursor.execute(query, [b])
        connection.commit()


