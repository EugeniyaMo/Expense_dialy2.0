import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QInputDialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Expense_diary.ui', self)
        self.sum = 0
        self.expenceButton.clicked.connect(self.expence)
        self.incomeButton.clicked.connect(self.income)
        #self.deleteButton.clicked.connect(self.delete)

    def expence(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Добавить расход", "Введите сумму вашего расхода:"
        )
        if okBtnPressed:
            self.categoryExpense()

    def categoryExpense(self):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Категория расхода:",
            "Выберете категорию расхода:",
            ("Питание", "Транспорт", "Постоянные расходы"),
            0,
            False
        )
        if okBtnPressed:
            self.textExpense = i
            self.categoryBalance()

    def income(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Добавить доход", "Введите сумму вашего дохода:"
        )
        if okBtnPressed:
            self.categoryIncome()

    def categoryIncome(self):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Категория дохода:",
            "Выберете категорию дохода:",
            ("Заработная плата", "Аванс", "Премия"),
            0,
            False
        )
        if okBtnPressed:
            self.textIncome = i
            self.categoryBalance()

    def categoryBalance(self):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Категория баланса:",
            "Выберете категорию баланса:",
            ("Наличные", "Карта"),
            0,
            False
        )
        if okBtnPressed:
            self.textIncome = i
            self.tratment()

    def treatment(self):
        f = open("data.txt", mode="rb")
        self.dict = {}
        for i in range(8):
            s = f.readline().split()
            self.dict[s[0]] = s[1]
        f.close()

    def delete(self):
        #обнулять все значение из файла
        pass


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
