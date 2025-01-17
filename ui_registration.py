# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Registration(object):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(1005, 638)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Registration)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_18 = QtWidgets.QFrame(Registration)
        self.frame_18.setStyleSheet("\n"
"border-radius: 15px;\n"
"background-color: rgb(212, 212, 255);\n"
"\n"
"")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_8.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_18)
        self.stackedWidget.setObjectName("stackedWidget")
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.login)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.login)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.loginEdit = QtWidgets.QLineEdit(self.login)
        self.loginEdit.setStyleSheet("height: 50px;\n"
"background-color:white;\n"
"border-radius:5px;\n"
"border: 2px solid gray;\n"
"font: 30pt;")
        self.loginEdit.setObjectName("loginEdit")
        self.verticalLayout_4.addWidget(self.loginEdit)
        self.passwordEdit = QtWidgets.QLineEdit(self.login)
        self.passwordEdit.setStyleSheet("height: 50px;\n"
"background-color:white;\n"
"border-radius:5px;\n"
"border: 2px solid gray;\n"
"font: 30pt;")
        self.passwordEdit.setObjectName("passwordEdit")
        self.verticalLayout_4.addWidget(self.passwordEdit)
        self.loginIncorrectText = QtWidgets.QLabel(self.login)
        self.loginIncorrectText.setEnabled(True)
        self.loginIncorrectText.setStyleSheet("     font-weight: bold;\n"
"     font-size: 25px;")
        self.loginIncorrectText.setObjectName("loginIncorrectText")
        self.verticalLayout_4.addWidget(self.loginIncorrectText)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.login)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.registrationButton = QtWidgets.QPushButton(self.login)
        self.registrationButton.setStyleSheet("      height: 50px;\n"
"     width: 200px;\n"
"      box-sizing: border-box;\n"
"     background-color: white;\n"
"      border-radius: 5px;\n"
"     font-weight: bold;\n"
"     font-size: 25px;\n"
"")
        self.registrationButton.setObjectName("registrationButton")
        self.horizontalLayout.addWidget(self.registrationButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.enterButton = QtWidgets.QPushButton(self.login)
        self.enterButton.setStyleSheet("      height: 50px;\n"
"     width: 200px;\n"
"      box-sizing: border-box;\n"
"     background-color: white;\n"
"      border-radius: 5px;\n"
"     font-weight: bold;\n"
"     font-size: 25px;\n"
"")
        self.enterButton.setObjectName("enterButton")
        self.verticalLayout_4.addWidget(self.enterButton)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.stackedWidget.addWidget(self.login)
        self.registration1 = QtWidgets.QWidget()
        self.registration1.setObjectName("registration1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.registration1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.registration1)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.loginRegEdit = QtWidgets.QLineEdit(self.registration1)
        self.loginRegEdit.setStyleSheet("height: 50px;\n"
"background-color:white;\n"
"border-radius:5px;\n"
"border: 2px solid gray;\n"
"font: 30pt;")
        self.loginRegEdit.setObjectName("loginRegEdit")
        self.verticalLayout_3.addWidget(self.loginRegEdit)
        self.paswordRegEdit = QtWidgets.QLineEdit(self.registration1)
        self.paswordRegEdit.setStyleSheet("height: 50px;\n"
"background-color:white;\n"
"border-radius:5px;\n"
"border: 2px solid gray;\n"
"font: 30pt;")
        self.paswordRegEdit.setObjectName("paswordRegEdit")
        self.verticalLayout_3.addWidget(self.paswordRegEdit)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.regNextButton = QtWidgets.QPushButton(self.registration1)
        self.regNextButton.setStyleSheet("      height: 50px;\n"
"     width: 200px;\n"
"      box-sizing: border-box;\n"
"     background-color: white;\n"
"      border-radius: 5px;\n"
"     font-weight: bold;\n"
"     font-size: 25px;\n"
"")
        self.regNextButton.setObjectName("regNextButton")
        self.verticalLayout_3.addWidget(self.regNextButton)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.registration1)
        self.registration2 = QtWidgets.QWidget()
        self.registration2.setObjectName("registration2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.registration2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.registration2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.nameEdit = QtWidgets.QLineEdit(self.registration2)
        self.nameEdit.setStyleSheet("height: 50px;\n"
"background-color:white;\n"
"border-radius:5px;\n"
"border: 2px solid gray;\n"
"font: 30pt;")
        self.nameEdit.setObjectName("nameEdit")
        self.verticalLayout_5.addWidget(self.nameEdit)
        self.secondnameEdit = QtWidgets.QLineEdit(self.registration2)
        self.secondnameEdit.setStyleSheet("height: 50px;\n"
"background-color:white;\n"
"border-radius:5px;\n"
"border: 2px solid gray;\n"
"font: 30pt;")
        self.secondnameEdit.setObjectName("secondnameEdit")
        self.verticalLayout_5.addWidget(self.secondnameEdit)
        self.ageEdit = QtWidgets.QLineEdit(self.registration2)
        self.ageEdit.setStyleSheet("height: 50px;\n"
"background-color:white;\n"
"border-radius:5px;\n"
"border: 2px solid gray;\n"
"font: 30pt;")
        self.ageEdit.setObjectName("ageEdit")
        self.verticalLayout_5.addWidget(self.ageEdit)
        self.heightEdit = QtWidgets.QLineEdit(self.registration2)
        self.heightEdit.setStyleSheet("height: 50px;\n"
"background-color:white;\n"
"border-radius:5px;\n"
"border: 2px solid gray;\n"
"font: 30pt;")
        self.heightEdit.setObjectName("heightEdit")
        self.verticalLayout_5.addWidget(self.heightEdit)
        self.weightEdit = QtWidgets.QLineEdit(self.registration2)
        self.weightEdit.setStyleSheet("height: 50px;\n"
"background-color:white;\n"
"border-radius:5px;\n"
"border: 2px solid gray;\n"
"font: 30pt;")
        self.weightEdit.setObjectName("weightEdit")
        self.verticalLayout_5.addWidget(self.weightEdit)
        self.genderComboBox = QtWidgets.QComboBox(self.registration2)
        self.genderComboBox.setStyleSheet("#genderComboBox{\n"
"    height: 50px;\n"
"    background-color:white;\n"
"    border-radius:5px;\n"
"    border: 2px solid gray;\n"
"    font: 30pt;\n"
"}\n"
"\n"
"#genderComboBox::drop-down{\n"
"    border: 0px;\n"
"}\n"
"\n"
"#genderComboBox::down-arrow{\n"
"    image: url(:/icon/img/arrowdown.png);\n"
"    width: 12px;\n"
"    height:12px;\n"
"    margin-right: 15px;    \n"
"}\n"
"\n"
"#genderComboBox::on{\n"
"    border:4px solid #c2dbfe;\n"
"}\n"
"\n"
"#genderComboBox QListView{\n"
"    font-size:12px;\n"
"    border: 1px solid rgba(0,0,0,10%);\n"
"    padding: 5px;\n"
"    background-color:#fff;\n"
"    outline:0px;\n"
"}\n"
"\n"
"#genderComboBox QListView::item {\n"
"    paddiong-left: 10px;\n"
"    background-color: #fff\n"
"}\n"
"\n"
"#genderComboBox QListView::item:hover {\n"
"    background-color:#1e90ff;\n"
"}\n"
"\n"
"#genderComboBox QListView::item:selected {\n"
"    background-color:#1e90ff;\n"
"}")
        self.genderComboBox.setDuplicatesEnabled(False)
        self.genderComboBox.setFrame(True)
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.verticalLayout_5.addWidget(self.genderComboBox)
        self.regIncorrectText = QtWidgets.QLabel(self.registration2)
        self.regIncorrectText.setStyleSheet("     font-weight: bold;\n"
"     font-size: 25px;")
        self.regIncorrectText.setObjectName("regIncorrectText")
        self.verticalLayout_5.addWidget(self.regIncorrectText)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.regEndButton = QtWidgets.QPushButton(self.registration2)
        self.regEndButton.setStyleSheet("      height: 50px;\n"
"     width: 200px;\n"
"      box-sizing: border-box;\n"
"     background-color: white;\n"
"      border-radius: 5px;\n"
"     font-weight: bold;\n"
"     font-size: 25px;\n"
"")
        self.regEndButton.setObjectName("regEndButton")
        self.verticalLayout_5.addWidget(self.regEndButton)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.stackedWidget.addWidget(self.registration2)
        self.verticalLayout_8.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_18)

        self.retranslateUi(Registration)
        self.stackedWidget.setCurrentIndex(0)
        self.genderComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Dialog"))
        self.label_3.setText(_translate("Registration", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Вход</span></p></body></html>"))
        self.loginEdit.setPlaceholderText(_translate("Registration", "Логин"))
        self.passwordEdit.setPlaceholderText(_translate("Registration", "Пароль"))
        self.loginIncorrectText.setText(_translate("Registration", "<html><head/><body><p>⠀</p></body></html>"))
        self.label_4.setText(_translate("Registration", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Не зарегистрированы?</span></p></body></html>"))
        self.registrationButton.setText(_translate("Registration", "Регистрация"))
        self.enterButton.setText(_translate("Registration", "Войти"))
        self.label.setText(_translate("Registration", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Регистрация</span></p></body></html>"))
        self.loginRegEdit.setPlaceholderText(_translate("Registration", "Логин"))
        self.paswordRegEdit.setPlaceholderText(_translate("Registration", "Пароль"))
        self.regNextButton.setText(_translate("Registration", "Продолжить"))
        self.label_2.setText(_translate("Registration", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Регистрация</span></p></body></html>"))
        self.nameEdit.setPlaceholderText(_translate("Registration", "Имя"))
        self.secondnameEdit.setPlaceholderText(_translate("Registration", "Фамилия"))
        self.ageEdit.setPlaceholderText(_translate("Registration", "Возраст"))
        self.heightEdit.setPlaceholderText(_translate("Registration", "Рост"))
        self.weightEdit.setPlaceholderText(_translate("Registration", "Вес"))
        self.genderComboBox.setCurrentText(_translate("Registration", "Мужчина"))
        self.genderComboBox.setItemText(0, _translate("Registration", "Мужчина"))
        self.genderComboBox.setItemText(1, _translate("Registration", "Женщина"))
        self.regIncorrectText.setText(_translate("Registration", "⠀"))
        self.regEndButton.setText(_translate("Registration", "Завершить"))
import resources_rc
