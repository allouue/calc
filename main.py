from operator import itemgetter
import datetime
from datetime import date
import about
import sqlite3
import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import registration

from ui_splash_screen_adaptive import Ui_Main # Файл интерфейса

class Main(QDialog):
    def __init__(self):
        super().__init__()
        QDialog.__init__(self)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.setWindowTitle("Главная")
        self.connection = sqlite3.connect('./db/my_database.db')
        self.c = self.connection.cursor()
        self.user()
        self.ui.welcomeUser.setText("Здравствуйте, " + self.name)
        self.number = 0
        self.progress = 0
        self.weight_loss = 210 #средний сброс веса в день при потреблении 1200 ккал в граммах
        self.normal_protein = 1.3
        self.normal_fat = 1
        self.normal_carbo = 2
        self.show()
        self.showMain()

        # ---КНОПКИ ВЫБОРА В ГЛАВНОМ МЕНЮ---#
        self.ui.mainButton.clicked.connect(self.showMain)
        self.ui.mealButton.clicked.connect(self.showMeal)
        self.ui.hungerButton.clicked.connect(self.showHunger)
        self.ui.resultButton.clicked.connect(self.showResult)
        self.ui.switchAccount.clicked.connect(self.switchAccount)
        self.ui.aboutButton.clicked.connect(self.showAbout)

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

    # ---ПЕРЕКЛЮЧЕНИЕ СТРАНИЦ---#
    def showMain(self):
        try:
            #устанавливает количество приемов пищи за день
            self.ui.PPLabel.setText(str(len(self.c.execute(
                "SELECT * FROM products WHERE user_id = (?) and date = (?)",
                (self.id, date.today())).fetchall())) + " приемов пищи")
            # определяет нужное количество белков, жиров и углеводов в зависимости от веса пользователя
            maximum_protein = int(self.normal_protein * self.c.execute(
                "SELECT weight FROM users_stats WHERE user_id = (?)",
                (self.id,)).fetchone()[0])
            maximum_fat = int(self.normal_fat * self.c.execute(
                "SELECT weight FROM users_stats WHERE user_id = (?)",
                (self.id,)).fetchone()[0])
            maximum_carbo = int(self.normal_carbo * self.c.execute(
                "SELECT weight FROM users_stats WHERE user_id = (?)",
                (self.id,)).fetchone()[0])
            # ставит нужное количество белков как максимум и ставит в прогрессбар число употребленных белков
            self.ui.progressBar_Protein.setRange(0, maximum_protein)
            self.ui.progressBar_Protein.setValue(int(sum(list(map(itemgetter(0),
                                                 self.c.execute("SELECT protein FROM products WHERE user_id = (?) and date = (?)",
                                       (self.id, date.today())).fetchall())))))
            # то же самое для жиров
            self.ui.progressBar_Fat.setRange(0, maximum_fat)
            self.ui.progressBar_Fat.setValue(int(sum(list(map(itemgetter(0),
                                             self.c.execute("SELECT fat FROM products WHERE user_id = (?) and date = (?)",
                                   (self.id, date.today())).fetchall())))))
            # то же самое для углеводов
            self.ui.progressBar_Carbohydrates.setRange(0, maximum_carbo)
            self.ui.progressBar_Carbohydrates.setValue(int(sum(list(map(itemgetter(0),
                                                              self.c.execute(
                                                                  "SELECT carbohydrates FROM products WHERE user_id = (?) and date = (?)",
                                                                  (self.id, date.today())).fetchall())))))
        except Exception as e:
            print(e)
        self.ui.stackedWidgetMain.setCurrentWidget(self.ui.mainPage)

        self.progressBarValue()

    def showMeal(self):
        self.ui.stackedWidgetMain.setCurrentWidget(self.ui.mealPage)
        #так как первый экран-завтрак, то тут сразу выводит его данные
        try:
            self.break_data = self.c.execute("SELECT * FROM products WHERE user_id = (?) and category = (?) and date = (?)",
                                        (self.id, "Завтрак", date.today())).fetchone()
            if self.break_data[2] == "Завтрак":
                self.ui.breakName.setText(self.break_data[1].title())
                self.ui.breakCalories.setText("Калории: " + str(self.break_data[3]))
                self.ui.breakProtein.setText("Белки: " + str(self.break_data[4]))
                self.ui.breakFat.setText("Жиры: " + str(self.break_data[5]))
                self.ui.breakCarbo.setText("Углеводы: " + str(self.break_data[6]))
        except Exception as e:
            print(e)

    def showHunger(self):
        self.ui.stackedWidgetMain.setCurrentWidget(self.ui.hungerPage)

    def showResult(self):
        self.ui.stackedWidgetMain.setCurrentWidget(self.ui.resultPage)
        # берет по порядку калории белки жиры углеводы, суммирует и выводит на экран
        try:
            self.ui.totalCalories.setText("Калории: " + str(
                sum(list(map(itemgetter(0), self.c.execute("SELECT calories FROM products WHERE user_id = (?) and date = (?)",
                           (self.id, date.today())).fetchall())))))
            self.ui.totalProtein.setText("Белки: " + str(
                sum(list(map(itemgetter(0), self.c.execute("SELECT protein FROM products WHERE user_id = (?) and date = (?)",
                                                           (self.id, date.today())).fetchall())))))
            self.ui.totalFat.setText("Жиры: " + str(
                sum(list(map(itemgetter(0), self.c.execute("SELECT fat FROM products WHERE user_id = (?) and date = (?)",
                                                           (self.id, date.today())).fetchall())))))
            self.ui.totalCarbo.setText("Углеводы: " + str(
                sum(list(map(itemgetter(0), self.c.execute("SELECT carbohydrates FROM products WHERE user_id = (?) and date = (?)",
                                                           (self.id, date.today())).fetchall())))))
            self.ui.congrats.setAlignment(QtCore.Qt.AlignCenter)
            # считает количество дней в текущем месяце, сколько пользователь ел
            days_total = len(self.c.execute("SELECT id FROM products WHERE date LIKE (?) and user_id = (?)",
                           ('%'+str(date.today().month)+'%', self.id)).fetchall())
            self.ui.congrats.setText(str(((self.weight_loss*days_total)/3)/1000))
        except Exception as e:
            print(e)

    # Переключение страниц внутри страницы mealPage
    def showMealBreakPage(self):
        self.ui.stackedWidgetMeal.setCurrentWidget(self.ui.meal_breakPage)

    def showMealDinnerPage(self):
        self.ui.stackedWidgetMeal.setCurrentWidget(self.ui.meal_dinnerPage)
        try:
            self.break_data = self.c.execute("SELECT * FROM products WHERE user_id = (?) and category = (?) and date = (?)",
                                        (self.id, "Обед", date.today())).fetchone()
            if self.break_data[2] == "Обед":
                self.ui.dinnerName.setText(self.break_data[1].title())
                self.ui.dinnerCalories.setText("Калории: " + str(self.break_data[3]))
                self.ui.dinnerProtein.setText("Белки: " + str(self.break_data[4]))
                self.ui.dinnerFat.setText("Жиры: " + str(self.break_data[5]))
                self.ui.dinnerCarbo.setText("Углеводы: " + str(self.break_data[6]))
        except Exception as e:
            print(e)

    def showMealEmealPage(self):
        self.ui.stackedWidgetMeal.setCurrentWidget(self.ui.meal_emealPage)
        try:
            self.break_data = self.c.execute("SELECT * FROM products WHERE user_id = (?) and category = (?) and date = (?)",
                                        (self.id, "Ужин", date.today())).fetchone()
            if self.break_data[2] == "Ужин":
                self.ui.emealName.setText(self.break_data[1].title())
                self.ui.emealCalories.setText("Калории: " + str(self.break_data[3]))
                self.ui.emealProtein.setText("Белки: " + str(self.break_data[4]))
                self.ui.emealFat.setText("Жиры: " + str(self.break_data[5]))
                self.ui.emealCarbo.setText("Углеводы: " + str(self.break_data[6]))
        except Exception as e:
            print(e)

    def showMealSnackPage(self):
        try:
            self.break_data = self.c.execute("SELECT * FROM products WHERE user_id = (?) and category = (?) and date = (?)",
                                        (self.id, "Перекус", date.today())).fetchone()
            if self.break_data[2] == "Перекус":
                self.ui.snackName.setText(self.break_data[1].title())
                self.ui.snackCalories.setText("Калории: " + str(self.break_data[3]))
                self.ui.snackProtein.setText("Белки: " + str(self.break_data[4]))
                self.ui.snackFat.setText("Жиры: " + str(self.break_data[5]))
                self.ui.snackCarbo.setText("Углеводы: " + str(self.break_data[6]))
        except Exception as e:
            print(e)
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
        try:
            # Добавляем в БД
            self.c.execute("""
                   INSERT INTO Products (food_name, category, calories, protein, fat, carbohydrates, date, user_id) VALUES ((?), (?), (?), (?), (?), (?), (?), (?))
                   """,
        (self.ui.lineEdit.text(),
                  category,
                  int(self.ui.add_calorieLine_.text()),
                  int(self.ui.add_proteinLine_.text()),
                  int(self.ui.add_fatLine_.text()),
                  int(self.ui.add_chLine_.text()),
                  date.today(),
                  int(self.id)))
            self.connection.commit()
        except Exception as e:
            print(e)
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
    def progressBarValue(self):
        try:
            # Стиль прогрессбара с указанием остановок
            styleSheet = """
            QFrame{
                border-radius: 80px;
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(0, 0, 0, 0), stop:{STOP_2} rgba(255, 255, 255, 255));
            }
            """
            self.value = int(sum(list(map(itemgetter(0),
                                                     self.c.execute("SELECT calories FROM products WHERE user_id = (?) and date = (?)",
                                           (self.id, date.today())).fetchall()))))
            if self.value > 1200:
                self.value = 1200
            # Взять значение прогрессбара и конвертировать в float
            if self.value != 0:
                self.progress = abs(1200 - self.value) / 1000.0
            else:
                self.progress = 0.5
            print("прогресс: " + str(self.progress))
            # Назначение чисел прогрессбару
            self.stop_1 = str(self.progress - 0.001)  # 0.001 для корректной работы
            self.stop_2 = str(self.progress)
            print(self.stop_1, self.stop_2)
            newStylesheet = styleSheet.replace("{STOP_1}", self.stop_1).replace("{STOP_2}", self.stop_2) #заменяем
            self.ui.CircularProgressBar.setStyleSheet(newStylesheet) #применяем
        except Exception as e:
            print(e)
            print("здесь")

    def showAbout(self):
        try:
            self.mainInterface = about.About()
            self.mainInterface.show()
        except Exception as e:
            print(e)

    def switchAccount(self):
        try:
            self.mainInterface = registration.Registration()
            self.mainInterface.show()
            self.close()
        except Exception as e:
            print(e)

    # ---ОПРЕДЕЛЕНИЕ АКТИВНОГО ПОЛЬЗОВАТЕЛЯ---#
    def user(self):
        self.id = self.c.execute("SELECT id FROM users WHERE is_active = 1").fetchone()[0]
        print(self.id)
        self.name = self.c.execute("SELECT name FROM users_stats WHERE user_id = ((?))", (self.id,)).fetchone()[0]
        print(self.name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())