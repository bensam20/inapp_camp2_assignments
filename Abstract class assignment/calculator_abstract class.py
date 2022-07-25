from abc import ABC, abstractmethod

class Calculator(ABC):

    @abstractmethod
    def calculator(self):
        pass

    @property
    def num1(self): 
        return self.__num1

    @num1.setter
    def num1(self, num):
        if(isinstance(num, int)):
            self.__num1 = num
        else:
            raise ValueError(f"Invalid operand(A)!")

    @property
    def num2(self): 
        return self.__num2

    @num2.setter
    def num2(self, num):
        if(isinstance(num, int)):
            self.__num2 = num
        else:
            raise ValueError(f"Invalid operand(B)!")

class CalcSum(Calculator):
    def calculator(self):
        print(f"Addition result : {self.num1 + self.num2}")

class CalcDiff(Calculator):
    def calculator(self):
        print(f"Subtraction result : {self.num1 - self.num2}")

class CalcProd(Calculator):
    def calculator(self):
        print(f"Multiplication result : {self.num1 * self.num2}")

class CalcQuo(Calculator):
    def calculator(self):
        print(f"Division result : {self.num1 / self.num2}")

#creating the object
add = CalcSum()
sub = CalcDiff()
mul = CalcProd()
div = CalcQuo()

add.num1 = 10
add.num2 = 5
add.calculator()

sub.num1 = 10
sub.num2 = 5
sub.calculator()

mul.num1 = 10
mul.num2 = 5
mul.calculator()

div.num1 = 10
div.num2 = 5
div.calculator()



