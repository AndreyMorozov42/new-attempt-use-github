class Calc:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation
        self.info_error = None

        if self.operation == "+":
            self.result = self.a + self.b
        elif self.operation == "-":
            self.result = self.a - self.b
        elif self.operation == "*":
            self.result = self.a * self.b
        elif self.operation == "/":
            self.result = self.a / self.b
        else:
            self.call_info()

    def call_info(self):
        self.info_error = True


if __name__ == "__main__":
    c = Calc(a=1, b=2, operation="-")
    print(c.result)
