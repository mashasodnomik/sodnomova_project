import sys
import sqlite3
from PyQt5 import QtCore, QtMultimedia, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QSlider, QWidget
from musplay import Ui_MainWindow
from playlistcreater import Ui_Form
import os


class MainWindow(QMainWindow, Ui_MainWindow, QListWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        super(QListWidget, self).__init__()
        self.setupUi(self)
        self.initui()

    def initui(self):
        self.list_of_genres.itemClicked.connect(self.click)
        self.list_of_songs.itemClicked.connect(self.musplay)
        self.pause.clicked.connect(self.muspause)
        self.next_song.clicked.connect(self.play_next_song)
        self.previous_song.clicked.connect(self.play_previous_song)
        self.flag = True
        self.volum.valueChanged.connect(self.change_volum)
        self.playlists = {}

    def change_volum(self, value):
        self.player.setVolume(value)

    def musplay(self, item):
        print(item.text())
        os.remove("C://Users//USER//PycharmProjects//project//test_out3.wav")
        self.current_song.setText(f"{item.text()}")
        self.flag = True
        with open("test_out3.wav", "wb") as wav_out:
            connection = sqlite3.connect("projectmusic.db")
            cursor = connection.cursor()
            result = cursor.execute(f"""SELECT (bytes) FROM TRACK WHERE name_track = "{item.text()}" """).fetchone()
            wav_out.write(result[0])
            self.player = QtMultimedia.QMediaPlayer()
            self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("test_out3.wav")))
            self.player.play()

    def muspause(self):
        if self.flag == True:
            self.pause.setText("PLAY")
            self.player.pause()
            self.flag = False
        elif self.flag == False:
            self.pause.setText("PAUSE")
            self.player.play()
            self.flag = True

    def play_next_song(self):
        n = self.list_of_songs.currentRow()
        self.list_of_songs.setCurrentRow(n+1)
        m = self.list_of_songs.currentRow()
        if m == self.list_of_songs.count():
            self.list_of_songs.setCurrentRow(0)
        self.musplay(self.list_of_songs.currentItem())


    def play_previous_song(self):
        n = self.list_of_songs.currentRow()
        self.list_of_songs.setCurrentRow(n - 1)
        m = self.list_of_songs.currentRow()
        if m == self.list_of_songs.count():
            self.list_of_songs.setCurrentRow(0)
        self.musplay(self.list_of_songs.currentItem())

    def click(self, item):
        self.list_of_songs.clear()
        if item.text() == "POP MUSIC":
            pop_songs = []
            connection = sqlite3.connect("projectmusic.db")
            cursor = connection.cursor()
            result = cursor.execute("""SELECT (name_track) FROM TRACK WHERE id_genre = 1 """).fetchall()
            for elem in result:
                pop_songs.append(str(elem[0]))
            self.list_of_songs.addItems(pop_songs)
        elif item.text() == "HIP-HOP MUSIC":
            hiphop_songs = []
            connection = sqlite3.connect("projectmusic.db")
            cursor = connection.cursor()
            result = cursor.execute("""SELECT (name_track) FROM TRACK WHERE id_genre = 6""").fetchall()
            for elem in result:
                hiphop_songs.append(str(elem[0]))
            self.list_of_songs.addItems(hiphop_songs)
        elif item.text() == "ROCK MUSIC":
            rock_songs = []
            connection = sqlite3.connect("projectmusic.db")
            cursor = connection.cursor()
            result = cursor.execute("""SELECT (name_track) FROM TRACK WHERE id_genre = 2""").fetchall()
            for elem in result:
                rock_songs.append(str(elem[0]))
            self.list_of_songs.addItems(rock_songs)
        elif item.text() == "RnB MUSIC":
            rnb_songs = []
            connection = sqlite3.connect("projectmusic.db")
            cursor = connection.cursor()
            result = cursor.execute("""SELECT (name_track) FROM TRACK WHERE id_genre = 3""").fetchall()
            for elem in result:
                rnb_songs.append(str(elem[0]))
            self.list_of_songs.addItems(rnb_songs)
        elif item.text() == "LO_FI AND BEATS":
            lofi_beats_songs = []
            connection = sqlite3.connect("projectmusic.db")
            cursor = connection.cursor()
            result = cursor.execute("""SELECT (name_track) FROM TRACK WHERE id_genre = 4""").fetchall()
            for elem in result:
                lofi_beats_songs.append(str(elem[0]))
            self.list_of_songs.addItems(lofi_beats_songs)
        elif item.text() == "CLASSICAL MUSIC":
            classical_songs = []
            connection = sqlite3.connect("projectmusic.db")
            cursor = connection.cursor()
            result = cursor.execute("""SELECT (name_track) FROM TRACK WHERE id_genre = 5""").fetchall()
            for elem in result:
                classical_songs.append(str(elem[0]))
            self.list_of_songs.addItems(classical_songs)
        elif item.text() == "ADD NEW PLAYLIST":
            self.crpplay = Widget()
            self.crpplay.show()
            if os.path.getsize("C://Users//USER//PycharmProjects//project//playlist.txt") == 0:
                pass
            else:
                self.cr_pl()

        else:
            print(self.playlists)
            for i in range(len(list(self.playlists.keys()))):
                if item.text() == str(list(self.playlists.keys())[i]):
                    for elem in list(map(lambda x: self.playlists[x] ,self.playlists.keys())):
                        for i in range(len(elem)):
                            self.list_of_songs.addItem(elem[i].rstrip())

    def cr_pl(self):
        with open("playlist.txt", "r") as f:
            playlist_songs = list(f.readlines())
        playlist_name = playlist_songs[0]
        playlist_songs.remove(playlist_songs[0])
        self.list_of_genres.addItem(playlist_name.rstrip())
        self.playlists[f"{playlist_name.rstrip()}"] = playlist_songs

class Widget(QWidget, Ui_Form):
    def __init__(self):
        super(Widget, self).__init__()
        super(MainWindow).__init__()
        self.setupUi(self)
        self.initui()
        self.lst = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5,  self.checkBox_6,
               self.checkBox_7, self.checkBox_8, self.checkBox_9, self.checkBox_10, self.checkBox_11, self.checkBox_12,
               self.checkBox_13, self.checkBox_14, self.checkBox_15, self.checkBox_16, self.checkBox_17, self.checkBox_18,
               self.checkBox_19, self.checkBox_20, self.checkBox_20, self.checkBox_21, self.checkBox_22, self.checkBox_23,
               self.checkBox_24, self.checkBox_25, self.checkBox_26, self.checkBox_27, self.checkBox_28, self.checkBox_29,
               self.checkBox_30, self.checkBox_31, self.checkBox_32, self.checkBox_33, self.checkBox_34, self.checkBox_35,
               self.checkBox_36, self.checkBox_37, self.checkBox_38, self.checkBox_39, self.checkBox_40]

    def initui(self):
        connection = sqlite3.connect("projectmusic.db")
        cursor = connection.cursor()
        result = cursor.execute("""SELECT (name_track) FROM TRACK""").fetchall()
        self.add_song.clicked.connect(self.create_playlist)

    def create_playlist(self):
        with open("playlist.txt", "w") as f:
            f.write(f"{self.lineEdit.text()}\n")
            for elem in self.lst:
                if elem.isChecked():
                    f.writelines(f"{elem.text()}\n")
        self.hide()









    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())


