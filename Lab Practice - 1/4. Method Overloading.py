
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





