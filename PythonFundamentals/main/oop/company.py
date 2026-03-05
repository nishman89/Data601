

class Company:

    def __init__(self, name):
        self._name = name
        self._employees =[]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def employees(self):
        return self._employees

    def add_employee(self, person):
        self._employees.append(person)
