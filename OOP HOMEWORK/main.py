class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):

        if self.b != 0:
            print(self.a // self.b)
        else:
            print("ZeroDivisionError: b cannot be zero")

    def subtraction(self):

        print(self.a - self.b)


m = Math(10, 5)

m.addition()  # 15
m.multiplication()  # 50
m.division()  # 2.0
m.subtraction()  # 5
