from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from system import System
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.vertical_labels = []
        self.horizontal_labels = []
        self.count = 1
        self.create_table()
        self.pushButton.clicked.connect(self.get_result)

    def create_table(self):
        # Устанавливаем количество строк и столбцов
        self.tableWidget.setRowCount(4)  # Для примера, 4 строки
        self.tableWidget.setColumnCount(5)  # Два столбца
        # Устанавливаем названия столбцов
        self.tableWidget.setHorizontalHeaderLabels(["Кол-во голосов","Геккон", "Попугай", "Хомяк", "Рыбки"])
        self.tableWidget.setVerticalHeaderLabels(["1 гр. экспертов:","2 гр. экспертов:","3 гр. экспертов:","4 гр. экспертов:"])

    def get_result(self):
        # массив предпочтений агентов
        #preference_array = []
        preference_array = [[] for _ in range(self.tableWidget.rowCount())]
        # список голосов по группам
        self.vote_list = []
        for i in range(self.tableWidget.rowCount()):
            try:
                vote = int(self.tableWidget.item(i, 0).text())
                self.vote_list.append(vote)  # Исправлено создание и добавление значения
            except (AttributeError, TypeError, ValueError) as e:
                print(f"Ошибка при извлечении данных из ячейки: {e}")
        print(self.vote_list)
        for i in range(self.tableWidget.rowCount()):
            for j in range(1, self.tableWidget.columnCount()):
                try:
                    preference_array[i].append(
                        int(self.tableWidget.item(i, j).text()))
                except (AttributeError, TypeError, ValueError) as e:
                    print(f"Ошибка при извлечении данных из ячейки {i}, {j}: {e}")
        print(preference_array)
        print(len(preference_array[0]))
        system = System(preference_array,  self.vote_list)
        log = system.get_result()
        self.log(log)



    def log(self, log):
        self.textBrowser.clear()
        self.textBrowser.append(log)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 225, 600, 650))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 180, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 600, 145))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Модели коллективного принятия решения"))
        self.pushButton.setText(_translate("MainWindow", "Определить"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
