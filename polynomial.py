class Variable:
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return self.symbol


class Equation:
    ADD, SUB = ["+", "-"]

    def __init__(self, op, a, b):
        self.op = op
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} {self.op} {self.b}"

    def __add__(self, other):
        return Equation(Equation.ADD, self, other)

    def __sub__(self, other):
        return Equation(Equation.SUB, self, other)

    def __neg__(self):
        return Equation(self.op, -self.a, -self.b)

    def integrate(self):
        self.a.integrate()
        self.b.integrate()
        return self


class Polynomial(Variable):
    def __init__(self, symbol, coeff, deg):
        super().__init__(symbol)
        self.coeff = coeff
        self.deg = deg

    def __str__(self):
        return f"{self.coeff}{self.symbol}^{self.deg}"

    def __add__(self, other):
        return Equation(Equation.ADD, self, other)

    def __sub__(self, other):
        return Equation(Equation.SUB, self, other)

    def __neg__(self):
        return Polynomial(self.symbol, -self.coeff, self.deg)

    def integrate(self):
        self.deg += 1
        self.coeff /= self.deg
        return self
