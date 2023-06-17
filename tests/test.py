import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):                 #Сложение
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction(self):                    #Вычитание
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_division(self):                       #деление
        assert self.calc.division(self, 12, 6) == 2

    def test_multiply(self):                       #Умножение
        assert self.calc.multiply(self, 10, 30) == 300
    #
    # def test_adding_unsuccess(self):              #Неверный результат
    #     assert self.calc.adding(self, 1, 1) == 5
    #
    # def test_zero_division(self):                 #Деление на ноль запрещено, исключение
    #     with pytest.raises(ZeroDivisionError):
    #         self.calc.division(self, 55, 0)

    def teardown(self):
        print('Выполнено')