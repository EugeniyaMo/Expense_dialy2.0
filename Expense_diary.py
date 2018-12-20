import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QInputDialog, QErrorMessage
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
from PyQt5.QtGui import QIcon

COUNT_CATEGORY = 12

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Expense_diary.ui', self)
        self.setWindowTitle('Expense diary')
        self.setWindowIcon(QIcon('icon.png'))

        self.expenceButton.setStyleSheet("background-color: #ffd8bd")
        self.incomeButton.setStyleSheet("background-color: #ffd8bd")
        self.deleteButton.setStyleSheet("background-color: #edd0be")

        self.expenceButton.clicked.connect(self.expence)
        self.incomeButton.clicked.connect(self.income)
        self.f = 0

        self.data = open("data.txt", mode="r", encoding="utf-8").read()
        self.data = self.data.split('\n')
        for i in range(len(self.data)):
            self.data[i] = self.data[i].split()
        self.data = dict(self.data)
        self.printData()

        self.deleteButton.clicked.connect(self.deleteData)

    def printData(self):
        self.lcdNumber_cash.display(int(self.data['cash']))
        self.lcdNumber_card.display(int(self.data['card']))
        self.lcdNumber.display(int(self.data['cash']) + int(self.data['card']))
        self.lcdNumber_salary.display(int(self.data['salary']))
        self.lcdNumber_advance.display(int(self.data['advance']))
        self.lcdNumber_prize.display(int(self.data['prize']))
        self.lcdNumber_otherIn.display(int(self.data['otherIn']))
        self.lcdNumber_transport.display(int(self.data['transport']))
        self.lcdNumber_food.display(int(self.data['food']))
        self.lcdNumber_shoping.display(int(self.data['shoping']))
        self.lcdNumber_study.display(int(self.data['study']))
        self.lcdNumber_relax.display(int(self.data['relax']))
        self.lcdNumber_otherEx.display(int(self.data['otherEx']))
        self.lcdNumber_income.display(int(self.data['salary'])
                                      + int(self.data['advance'])
                                      + int(self.data['prize'])
                                      + int(self.data['otherIn']))
        self.lcdNumber_expense.display(int(self.data['transport'])
                                       + int(self.data['food'])
                                       + int(self.data['shoping'])
                                       + int(self.data['study'])
                                       + int(self.data['relax'])
                                       + int(self.data['otherEx']))

    def expence(self):
        self.f = -1
        i, okBtnPressed = QInputDialog.getText(
            self, "Добавить расход", "Введите сумму вашего расхода:"
        )
        if okBtnPressed:
            self.sumExpense = i
            self.categoryExpense()

    def categoryExpense(self):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Категория расхода",
            "Выберете категорию расхода:",
            ("Транспорт", "Питание", "Покупки", "Учеба", "Развлечения",
             "Другое"),
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
            ("Заработная плата", "Аванс", "Премия", "Другое"),
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
            ("Карта", "Наличные"),
            0,
            False
        )
        if okBtnPressed:
            self.textBalance = i
            self.processing()

    def processing(self):
        try:
            # обработка операции "Доход"
            if self.f == 1:
                if self.checkIncome():
                    if (self.textIncome == "Заработная плата"):
                        self.data['salary'] = str(int(self.data['salary']) + int(self.sumIncome))
                    elif (self.textIncome == "Аванс"):
                        self.data['advance'] = str(int(self.data['advance']) + int(self.sumIncome))
                    elif (self.textIncome == "Премия"):
                        self.data['prize'] = str(int(self.data['prize']) + int(self.sumIncome))
                    elif (self.textIncome == "Другое"):
                        self.data['otherIn'] = str(int(self.data['otherIn']) + int(self.sumIncome))
                    if (self.textBalance == "Наличные"):
                        self.data['cash'] = str(int(self.data['cash']) + int(self.sumIncome))
                    elif (self.textBalance == "Карта"):
                        self.data['card'] = str(int(self.data['card']) + int(self.sumIncome))
            # обработка операции "Расход"
            elif self.f == -1:
                if self.checkExpense():
                    if (self.textExpense == "Транспорт"):
                        self.data['transport'] = str(int(self.data['transport']) + int(self.sumExpense))
                    elif (self.textExpense == "Питание"):
                        self.data['food'] = str(int(self.data['food']) + int(self.sumExpense))
                    elif (self.textExpense == "Покупки"):
                        self.data['shoping'] = str(int(self.data['shoping']) + int(self.sumExpense))
                    elif (self.textExpense == "Учеба"):
                        self.data['study'] = str(int(self.data['study']) + int(self.sumExpense))
                    elif (self.textExpense == "Развлечения"):
                        self.data['relax'] = str(int(self.data['relax']) + int(self.sumExpense))
                    elif (self.textExpense == "Другое"):
                        self.data['otherEx'] = str(int(self.data['otherEx']) + int(self.sumExpense))
                    if (self.textBalance == "Наличные"):
                        self.data['cash'] = str(int(self.data['cash']) - int(self.sumExpense))
                    elif (self.textBalance == "Карта"):
                        self.data['card'] = str(int(self.data['card']) - int(self.sumExpense))
            # дисплей
            self.printData()
            self.changeFail()
            self.f = 0
        except Exception as e:
            pass

    def checkIncome(self):
        if int(self.sumIncome) > 0:
            return 1
        return 0

    def checkExpense(self):
        if int(self.sumExpense) > 0:
            if self.textBalance == "Наличные":
                if int(self.sumExpense) <= int(self.data['cash']):
                    return 1
            elif self.textBalance == "Карта":
                if int(self.sumExpense) <= int(self.data['card']):
                    return 1
        return 0

    def changeFail(self):
        try:
            f = open("data.txt", mode='w')
            name = ['cash', 'card', 'salary', 'advance', 'prize', 'otherIn',
                    'transport', 'food', 'shoping', 'study', 'relax', 'otherEx']
            for i in range(COUNT_CATEGORY):
                f.write(name[i] + ' ' + self.data[name[i]])
                if (i != COUNT_CATEGORY - 1):
                    f.write('\n')
            f.close()
        except Exception as e:
            pass

    def deleteData(self):
        try:
            i, okBtnPressed = QInputDialog.getItem(
                self,
                "Очистить данные",
                "Вы уверены, что хотите удалить всю информацию о своих расходах?",
                ("Да", "Нет"),
                0,
                False
            )
            if okBtnPressed:
                if (i == "Да"):
                    self.delete()
        except Exception as e:
            pass

    def delete(self):
        # обнулять все значение из файла
        try:
            name = ['cash', 'card', 'salary', 'advance', 'prize', 'otherIn',
                    'transport', 'food', 'shoping', 'study', 'relax', 'otherEx']
            for i in range(COUNT_CATEGORY):
                self.data[name[i]] = '0'
            self.changeFail()
            self.printData()
        except Exception as e:
            pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
