class Person:
    def __init__(self, name, age, city):
        #attributes
        self._name = name
        self._age = age
        self._city = city

    # In python, when functions are in classes they are referred to as methods!
    def greet(self):
        return f"Hello, my name is {self._name} and I am {self._age} years old from {self._city}"

    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    def __str__(self):
        return  f"Person details: name is {self._name} and I am {self._age} years old from {self._city}"


class Manager(Person):
    def __init__(self, name, age, city, department):
        super().__init__(name, age, city)
        self._department = department

    def manage(self):
        return f"{self.name} is managing the {self._department} department"

    def __str__(self):
        return f"is managing the {self._department} department"
