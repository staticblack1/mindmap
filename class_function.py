


class rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width

    def perimeter(self):
        return 2 * (self.lenght + self.width)

    def __str__(self):
        return F"the perimeter is {self.perimeter()}, the area is {self.area()}"

