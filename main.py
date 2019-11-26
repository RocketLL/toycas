from polynomial import *

if __name__ == "__main__":
    X = Polynomial("x", 2, 3)  # Creates X=2x^3
    Y = Polynomial("y", 4, 4)  # Creates Y=4y^4
    print(X + Y)  # Symbolically calculates X+Y
    print((X - Y).integrate())  # Symbolically calculates the antiderivative of X-Y

