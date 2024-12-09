class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    # Overloading the + operator
    def __add__(self, other):
        return str(self.real + other.real) + "+" + str(self.imaginary + other.imaginary) + "i"


# Creating two complex number objects
c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(4, 5)

# Using the overloaded + operator
print(c1 + c2)  # Output: 5+7i