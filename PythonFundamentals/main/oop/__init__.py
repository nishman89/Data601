from main.oop.company import Company
from main.oop.person import *

nish = Person("Nish Mandal", 36, "Birmingham")
nish.city = "London" #calling the setter method in city
ramim = Person("Ramim Mollah", 12, "Manchester")
erik = Person("Erik Kildare", 99, "Istanbul")

company = Company("Aisha Ltd")

company.add_employee(nish)
company.add_employee(ramim)
company.add_employee(erik)

for person in company.employees:
    print(f"{person.name}, from {person.city} and is {person.age} years old")

result = nish.greet()
print(nish.__str__())

abinash = Manager("Abinash", 40, "London", "HR")
print(abinash)