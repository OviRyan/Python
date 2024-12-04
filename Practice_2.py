print(1+2)
print("1" + "2")


def sqr(x):
    return x*x

print(sqr(5.5))


class Duck:
    def swim(self):
        print("I am a duck and I can swim")

    def speaks(self):
        print("Quack Quack")


class Dog:
    def swim(self):
        print("I am a dog and I can swim")

    def speaks(self):
        print("Woof Woof")


def display(duck):
    duck.swim()
    duck.speaks()
    print("Information displayed")


# Creating objects of Duck and Dog
dk = Duck()
dog = Dog()

# Passing objects to display function
display(dog)
display(dk)




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
