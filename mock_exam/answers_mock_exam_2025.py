Q1 = "False. Recipe is a class, not an object (and thus no instance)."

Q2 = "A"

Q3 = "D"

Q4 = "B"

Q5 = "False. SecretRecipe is a class derived from Recipe."

Q6 = "A"

Q7 = "D"

Q8 = "C. It calls the constructor with super().__init__(name)."

Q9 = "D"

Q10 = "D"

Q11 = "A"

Q12 = "C. Since there are no superclasses (in which case we could only access public and protected attributes, but not private of the superclass) we can access everything!"

Q13 = "B. Since classmethods don't get the self parameter, only the cls parameter."

Q14 = "C"

Q15 = "D"

Q16 = "A"


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def __add__(self, other):
        if self._height == other._height:
            return Rectangle(2 * self._width, self._height)
        else:
            raise ValueError

    def __str__(self):
        return f"Square(sides={self._height})"
