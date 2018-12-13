import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Expense_diary.ui', self)
        self.sum = 0
        self.expenceButton.clicked.connect(self.expence)
        self.incomeButton.clicked.connect(self.income)
        self.f = 0
        self.sumIncome = 0

        #self.lcdNumber.display(4)
        self.data = open("data.txt", mode="r", encoding="utf-8").read()
        self.data = self.data.split('\n')
        for i in range(len(self.data)):
            self.data[i] = self.data[i].split()
        self.data = dict(self.data)
        self.printData()
        
        #self.deleteButton.clicked.connect(self.delete)

    def printData(self):
        self.lcdNumber_cash.display(int(self.data['cash']))
        self.lcdNumber.display(int(self.data['cash']) + int(self.data['card']))
        self.lcdNumber_card.display(int(self.data['card']))
        self.lcdNumber_salary.display(int(self.data['salary']))
        self.lcdNumber_advance.display(int(self.data['advance']))
        self.lcdNumber_prize.display(int(self.data['prize']))
        self.lcdNumber_transport.display(int(self.data['transport']))
        self.lcdNumber_food.display(int(self.data['food']))
        self.lcdNumber_shoping.display(int(self.data['shoping']))
        self.lcdNumber_study.display(int(self.data['study']))
        self.lcdNumber_relax.display(int(self.data['relax']))
        self.lcdNumber_income.display(int(self.data['salary'])
                                      + int(self.data['advance'])
                                      + int(self.data['prize']))
        self.lcdNumber_expense.display(int(self.data['transport'])
                                       + int(self.data['food'])
                                       + int(self.data['shoping'])
                                       + int(self.data['study'])
                                       + int(self.data['relax']))

    def expence(self):
        self.f = -1
        i, okBtnPressed = QInputDialog.getText(
            self, "Добавить расход", "Введите сумму вашего расхода:"
        )
        if okBtnPressed:
            self.categoryExpense()

    def categoryExpense(self):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Категория расхода",
            "Выберете категорию расхода:",
            ("Транспорт", "Питание", "Покупки", "Учеба", "Развлечения"),
            0,
            False
        )
        if okBtnPressed:
            self.textExpense = i
            self.categoryBalance()

    def income(self):
        self.f = 1
        i, okBtnPressed = QInputDialog.getText(
            self, "Добавить доход", "Введите сумму вашего дохода:"
        )
        if okBtnPressed:
            self.sumIncome = i
            self.categoryIncome()

    def categoryIncome(self):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Категория дохода",
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
            "Категория баланса",
            "Выберете категорию баланса:",
            ("Наличные", "Карта"),
            0,
            False
        )
        if okBtnPressed:
            self.textBalance = i
            self.processing()

    def processing(self):
        #обработка операции "Доход"
        try:
            if (self.f == 1):
                if (self.textIncome == "Заработная плата"):
                    self.data['salary'] = str(int(self.data['salary']) + int(self.sumIncome))
                    print('ok')
                elif (self.textIncome == "Аванс"):
                    self.data['advance'] = str(int(self.data['advance']) + int(self.sumIncome))
                elif (self.textIncome == "Премия"):
                    self.data['prize'] = str(int(self.data['prize']) + int(self.sumIncome))
                if (self.textBalance == "Наличные"):
                    self.data['cash'] = str(int(self.data['cash']) + int(self.sumIncome))
                elif (self.textBalance == "Карта"):
                    self.data['card'] = str(int(self.data['card']) + int(self.sumIncome))
        except Exception as e:
            print(e)
        #обработка операции "Расход"
        if (self.f == -1):
            pass
        #дисплей
        self.printData()


    def delete(self):
        #обнулять все значение из файла
        pass


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

