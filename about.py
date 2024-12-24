import sys
import sqlite3
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_about import Ui_About # Файл интерфейса

class About(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_About()
        self.ui.setupUi(self)
        self.setWindowTitle("О программе")
        self.connection = sqlite3.connect('./db/my_database.db')
        self.c = self.connection.cursor()
        self.show()

        self.ui.deleteDB.clicked.connect(self.delete)
    def delete(self):
        try:
            self.c.executescript("""DELETE FROM products;
                              DELETE FROM users;
                              DELETE FROM users_stats""")
            self.connection.commit()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = About()
    sys.exit(app.exec_())