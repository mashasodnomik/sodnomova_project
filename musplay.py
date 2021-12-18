# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 670)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list_of_genres = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.list_of_genres.setFont(font)
        self.list_of_genres.setStyleSheet("QMainWindow{\n"
"border-image: url(C:/Users/USER/PycharmProjects/project/images2.jpg)\n"
"}")
        self.list_of_genres.setObjectName("list_of_genres")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_genres.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_genres.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_genres.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_genres.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_genres.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_genres.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_genres.addItem(item)
        self.horizontalLayout.addWidget(self.list_of_genres)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontal = QtWidgets.QVBoxLayout()
        self.horizontal.setObjectName("horizontal")
        self.list_of_songs = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_of_songs.setFont(font)
        self.list_of_songs.setObjectName("list_of_songs")
        self.horizontal.addWidget(self.list_of_songs)
        self.verticalLayout_2.addLayout(self.horizontal)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.current_song = QtWidgets.QLineEdit(self.centralwidget)
        self.current_song.setObjectName("current_song")
        self.verticalLayout.addWidget(self.current_song)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previous_song = QtWidgets.QPushButton(self.centralwidget)
        self.previous_song.setObjectName("previous_song")
        self.horizontalLayout_2.addWidget(self.previous_song)
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setObjectName("pause")
        self.horizontalLayout_2.addWidget(self.pause)
        self.next_song = QtWidgets.QPushButton(self.centralwidget)
        self.next_song.setObjectName("next_song")
        self.horizontalLayout_2.addWidget(self.next_song)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.volum = QtWidgets.QSlider(self.centralwidget)
        self.volum.setOrientation(QtCore.Qt.Vertical)
        self.volum.setObjectName("volum")
        self.horizontalLayout_3.addWidget(self.volum)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 865, 31))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.list_of_genres.isSortingEnabled()
        self.list_of_genres.setSortingEnabled(False)
        item = self.list_of_genres.item(0)
        item.setText(_translate("MainWindow", "POP MUSIC"))
        item = self.list_of_genres.item(1)
        item.setText(_translate("MainWindow", "HIP-HOP MUSIC"))
        item = self.list_of_genres.item(2)
        item.setText(_translate("MainWindow", "ROCK MUSIC"))
        item = self.list_of_genres.item(3)
        item.setText(_translate("MainWindow", "RnB MUSIC"))
        item = self.list_of_genres.item(4)
        item.setText(_translate("MainWindow", "CLASSICAL MUSIC"))
        item = self.list_of_genres.item(5)
        item.setText(_translate("MainWindow", "LO_FI AND BEATS "))
        item = self.list_of_genres.item(6)
        item.setText(_translate("MainWindow", "ADD NEW PLAYLIST"))
        self.list_of_genres.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "NOW PLAYING:"))
        self.previous_song.setText(_translate("MainWindow", "<<"))
        self.pause.setText(_translate("MainWindow", "PAUSE"))
        self.next_song.setText(_translate("MainWindow", ">>"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
