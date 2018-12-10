
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Expense_diary.ui', self)
        f = open("data.txt", mode="rb")
        f.close()
        self.expenceButton.clicked.connect(self.expence)
        self.incomeButton.clicked.connect(self.income)
        self.deleteButton.clicked.connect(self.delete)

    def expence(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Добавить расход", "Введите сумму вашего расхода"
        )
        if okBtnPressed:
            self.expenceButton.setInt(i)

    def income(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Добавить доход", "Введите сумму вашего дохода"
        )
        if okBtnPressed:
            self.incomeButton.setInt(i)

    def delete(self):
        #обнулять все значение из файла
        pass


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

