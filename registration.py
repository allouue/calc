from time import process_time

import main
import sqlite3
import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_registration import Ui_Registration # Файл интерфейса

class Registration(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Registration()
        self.ui.setupUi(self)
        self.show()
        self.setWindowTitle("Регистрация")
        self.check = 0

        # ---ДАТАБАЗА---#
        self.connection = sqlite3.connect('./db/my_database.db')
        self.cursor = self.connection.cursor()

        # ---СОЗДАНИЕ ТАБЛИЦ---#
        self.cursor.executescript('''
               CREATE TABLE IF NOT EXISTS Users 
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               login TEXT NOT NULL,
               password TEXT NOT NULL,
               is_active BOOLEAN);
               
               CREATE TABLE IF NOT EXISTS Users_Stats 
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               secondname TEXT NOT NULL,
               age INTEGER,
               gender TEXT NOT NULL,
               height INTEGER,
               weight INTEGER,
               user_id INTEGER,
               FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE);

               CREATE TABLE IF NOT EXISTS Products 
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               food_name TEXT NOT NULL,
               category TEXT NOT NULL,
               calories INTEGER,
               protein INTEGER,
               fat INTEGER,
               carbohydrates INTEGER,
               date INTEGER,
               user_id INTEGER,
               FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE);
               ''')
        self.connection.commit()

        # ---КНОПКИ РЕГИСТРАЦИИ---#
        self.ui.enterButton.clicked.connect(self.showMain)
        self.ui.registrationButton.clicked.connect(self.showRegistration)
        self.ui.regNextButton.clicked.connect(self.showNextRegistration)
        self.ui.regEndButton.clicked.connect(self.showLogin)

    # ---ОКНО ВВОДА---#
    def showMain(self):
        try:
            take = self.cursor.execute('SELECT * FROM users WHERE login = (?) AND password = (?)',
                                  (self.ui.loginEdit.text(),
                                             self.ui.passwordEdit.text())) # проверка на пользователя
            if take.fetchone() is not None:
                self.cursor.execute("""UPDATE users set is_active = 0 where is_active = 1""")
                self.connection.commit()
                self.cursor.execute(""" UPDATE users set is_active = 1 where login = (?) AND password = (?)""",
                                  (self.ui.loginEdit.text(),
                                             self.ui.passwordEdit.text()))
                self.connection.commit()
                self.mainInterface = main.Main()
                self.mainInterface.show()
                self.close()
            else:
                self.ui.loginIncorrectText.setText("Неправильный логин или пароль")
        except Exception as e:
            print(e)

    # ---ОТКРЫВАНИЕ ОКНА С РЕГИСТРАЦИЕЙ---#
    def showRegistration(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.registration1)

    # ---ОКНО РЕГИСТРАЦИИ С ЛОГИНОМ И ПАРОЛЕМ---#
    def showNextRegistration(self):
        try:
            take = self.cursor.execute('SELECT * FROM users WHERE login = (?) AND password = (?)',
                                       (self.ui.loginRegEdit.text(), self.ui.paswordRegEdit.text()))
            if take.fetchone() is not None: # проверка на существование пользователя
                print("пользователь уже есть")
            else:
                self.cursor.execute("""
                                                          INSERT INTO users (login, password, is_active) VALUES ((?), (?), (?))
                                                          """,
                                    (self.ui.loginRegEdit.text(),
                                     self.ui.paswordRegEdit.text(),
                                     0,
                                     ))
                self.connection.commit() # добавление пользователя
                self.login = self.ui.loginRegEdit.text() # передача логина в showLogin для автоназначения ключа пользователя
                self.ui.stackedWidget.setCurrentWidget(self.ui.registration2)
        except Exception as e:
            print(e)

    # ---ОКНО РЕГИСТРАЦИИ С ДАННЫМИ ПОЛЬЗОВАТЕЛЯ---#

    def showLogin(self):
        self.id = self.cursor.execute("SELECT id FROM users WHERE login = (?)", (self.login,)).fetchone()
        try:
            self.cursor.execute("""
                                      INSERT INTO users_stats (name, secondname, age, gender, height, weight, user_id) VALUES ((?), (?), (?), (?), (?), (?), (?))
                                      """, (self.ui.nameEdit.text(),
                                                      self.ui.secondnameEdit.text(),
                                                      int(self.ui.ageEdit.text()),
                                                      self.ui.genderComboBox.currentText(),
                                                      int(self.ui.heightEdit.text()),
                                                      int(self.ui.weightEdit.text()),
                                                      self.id[0]))
            self.connection.commit() # добавление данных пользователя
            self.ui.stackedWidget.setCurrentWidget(self.ui.login)
        except Exception as e:
            self.ui.regIncorrectText.setText("Введите числа в строки возраст, рост, вес")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Registration()
    sys.exit(app.exec_())