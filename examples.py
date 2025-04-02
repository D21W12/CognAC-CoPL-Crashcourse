class Person:

    # The constructor
    def __init__(
            self,
            first_name: str,
            last_name: str,
            age: int
    ):

        self.first_name = first_name  # Data attribute
        self.last_name = last_name  # Data attribute
        self.age = age  # Data attribute

    # Method
    def speak(self):
        print(f"Hey, my name is {self.first_name}!")

    # Operator overloading
    def __gt__(self, other):
        return self.age > other.age


class Student(Person):
    university = "Radboud"  # Class data attribute

    # The constructor
    def __init__(
            self,
            first_name: str,
            last_name: str,
            age: int,
            s_number: str
    ):

        # Calling the constructor of superclass
        super().__init__(first_name, last_name, age)
        self._s_number = s_number  # Protected

    @property
    def s_number(self):
        return self._s_number

    @s_number.setter
    def s_number(self, new_s_number):
        if new_s_number.startswith("s"):
            self._s_number = new_s_number
        else:
            raise ValueError

    def study(self):
        print(f"Student {self.__s_number} is studying!")

    # Method overriding
    def speak(self):
        print(f"Hey, my name is {self.first_name} and my s-number is {self.__s_number}!")

    @classmethod
    def print_univesity_slogan(cls):
        print(f"{cls.university} is amazing")


class TeachingAssistant(Student):

    # The constructor
    def __init__(
            self,
            first_name: str,
            last_name: str,
            age: int,
            s_number: str,
            e_number: str
    ):

        # Calling the constructor of superclass
        super().__init__(first_name, last_name, age, s_number)
        print(super().__class__)
        self._e_number = e_number

    def teach(self):
        print(f"TA {self.last_name} ({self.e_number}) is teaching!")
