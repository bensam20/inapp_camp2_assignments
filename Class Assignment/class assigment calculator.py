#defining the class
class Calculator:
    #add function
    def add(self, n1,n2):
        self.res=n1+n2
        print("Sum: ",self.res)
    #multiplication function
    def mul(self, n1,n2):
        self.res=n1*n2
        print("Product: ",self.res)
    #division function
    def div(self, n1,n2):
        self.res=n1/n2
        print("Quotient: ",self.res)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
#creating an object and calling the functions
calc1 = Calculator()
calc1.add(n1,n2)
calc1.mul(n1,n2)
calc1.div(n1,n2)