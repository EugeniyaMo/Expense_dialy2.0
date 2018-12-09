
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Expense_diary.ui', self)
        self.expenceButton.clicked.connect(self.expence)
        self.incomeButton.clicked.connect(self.income)
        self.deleteButton.clicked.connect(self.delete)

    def expence(self):
        #добавить к ОСТАТКУ сумму, введенную в диалоговое окно
        pass

    def income(self):
        #вычесть из ОСТАТКА сумму, введенную в диалоговое окно
        pass

    def delete(self):
        #обнулять все значение из файла
        pass


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

