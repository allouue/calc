import sqlite3
import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#файл интерфейса
from ui_splash_screen_adaptive import Ui_Dialog



class SplashScreen(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.number = 0


        # ---ДАТАБАЗА---#
        self.connection = sqlite3.connect('./db/my_database.db')
        self.cursor = self.connection.cursor()

        # ---СОЗДАНИЕ ТАБЛИЦ---#
        self.cursor.executescript('''
        CREATE TABLE IF NOT EXISTS Users 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL,
        password TEXT NOT NULL,
        name TEXT NOT NULL,
        secondname TEXT NOT NULL,
        age INTEGER,
        gender TEXT NOT NULL,
        height INTEGER,
        weight INTEGER);
        
        CREATE TABLE IF NOT EXISTS Products 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        food_name TEXT NOT NULL,
        category TEXT NOT NULL,
        calories INTEGER,
        protein INTEGER,
        fat INTEGER,
        carbohydrates INTEGER,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES Users (id) ON DELETE CASCADE);
        ''')
        self.connection.commit()


        # ---КНОПКИ ВЫБОРА В ГЛАВНОМ МЕНЮ---#
        self.ui.mainButton.clicked.connect(self.showMain)
        self.ui.mealButton.clicked.connect(self.showMeal)
        self.ui.hungerButton.clicked.connect(self.showHunger)
        self.ui.historyButton.clicked.connect(self.showHistory)
        self.ui.resultButton.clicked.connect(self.showResult)
        # self.ui.aboutButton.clicked.connect(self.showAbout)

        # ---КНОПКИ ДОБАВЛЕНИЯ ЕДЫ---#
        self.ui.meal_breakButton.clicked.connect(self.showMealBreakPage)
        self.ui.meal_dinnerButton.clicked.connect(self.showMealDinnerPage)
        self.ui.meal_emealButton.clicked.connect(self.showMealEmealPage)
        self.ui.meal_snackButton.clicked.connect(self.showMealSnackPage)
        #кнопки для отображения окна добавления еды
        self.ui.meal_addBreakButton.clicked.connect(self.showAdd)
        self.ui.meal_addDinnerButton.clicked.connect(self.showAdd)
        self.ui.meal_addEmealButton.clicked.connect(self.showAdd)
        self.ui.meal_addSnackButton.clicked.connect(self.showAdd)


        # ---КНОПКА ДОБАВЛЕНИЯ В БД---#
        self.ui.add_addMealButton.clicked.connect(self.addMeal)

    # ---ИЗМЕНЕНИЕ СТРАНИЦ---#
    def showMain(self):
        self.ui.stackedWidgetMain.setCurrentWidget(self.ui.mainPage)
    def showMeal(self):
        self.ui.stackedWidgetMain.setCurrentWidget(self.ui.mealPage)
    def showHunger(self):
        self.ui.stackedWidgetMain.setCurrentWidget(self.ui.hungerPage)
    def showHistory(self):
        self.ui.stackedWidgetMain.setCurrentWidget(self.ui.historyPage)
    def showResult(self):
        self.ui.stackedWidgetMain.setCurrentWidget(self.ui.resultPage)

    # Изменение страниц внутри страницы mealPage
    def showMealBreakPage(self):
        self.ui.stackedWidgetMeal.setCurrentWidget(self.ui.meal_breakPage)
    def showMealDinnerPage(self):
        self.ui.stackedWidgetMeal.setCurrentWidget(self.ui.meal_dinnerPage)
    def showMealEmealPage(self):
        self.ui.stackedWidgetMeal.setCurrentWidget(self.ui.meal_emealPage)
    def showMealSnackPage(self):
        self.ui.stackedWidgetMeal.setCurrentWidget(self.ui.meal_snackPage)

    # ---ДОБАВЛЕНИЕ В БАЗУ---#
    def addMeal(self):
        category = 0    # категория, которая задается в showAdd
        if self.number == 1:
            category = "Завтрак"
        elif self.number == 2:
            category = "Обед"
        elif self.number == 3:
            category = "Ужин"
        elif self.number == 4:
            category = "Перекус"

            # Добавляем в БД
            self.cursor.execute("""
                   INSERT INTO Products (food_name, category, calories, protein, fat, carbohydrates) VALUES ((?), (?), (?), (?), (?), (?))
                   """,
        (self.ui.lineEdit.text(),
                  int(self.ui.add_calorieLine_.text()),
                  int(self.ui.add_proteinLine_.text()),
                  int(self.ui.add_chLine_.text()),
                  int(self.ui.add_chLine_.text()),
                  int(self.ui.add_fatLine_.text())))
            self.connection.commit()
        # Переход на страницу mealPage
        self.ui.stackedWidgetMain.setCurrentWidget(self.ui.mealPage)

    # ---ОПРЕДЕЛЕНИЕ КАКОЙ ПЛЮСИК БЫЛ НАЖАТ---#
    def showAdd(self):
        self.ui.stackedWidgetMain.setCurrentWidget(self.ui.addPage)
        sender = self.sender()
        if sender.objectName() == "meal_addBreakButton":
            self.number = 1
        if sender.objectName() == "meal_addDinnerButton":
            self.number = 2
        if sender.objectName() == "meal_addEmealButton":
            self.number = 3
        if sender.objectName() == "meal_addSnackButton":
            self.number = 4


    # ---ПРОГРЕССБАР---#
    def progressBarValue(self, value):

        #стиль прогрессбара с указанием остановок
        styleSheet = """
        QFrame{
	        border-radius: 55px;
	        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(0, 0, 0, 0), stop:{STOP_2} rgba(255, 255, 255, 255));
        }
        """

        #взять значение прогрессбара и конвертировать в float
        progress = (100 - value) / 100.0

        #назначение чисел прогрессбару
        stop_1 = str(progress - 0.001) #0.001 для корректной работы
        stop_2 = str(progress)
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2) #заменяем
        self.ui.CircularProgressBar.setStyleSheet(newStylesheet) #применяем

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())