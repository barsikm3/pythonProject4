class Employees:
    name = ""
    surname = ""
    age = ""
    position = ""

person1 = Employees()
person1.name = "Elena"
person1.surname = "Kuchto"
person1.age = "33"
person1.position = "Manager"

person2 = Employees()
person2.name = "Siarhei"
person2.surname = "Pasiukevich"
person2.age = "37"
person2.position = "Specialist"

if person2.age < person1.age:
    print(print(person2.age))
else:
    print(person1.age)


def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list
print(list_animals("Big"))

def list_animals(animals):
    return ''.join('{}. {}\n'.format(i, x) for (i, x) in enumerate(animals, 1))
print(list_animals("Big"))

def list_animals(animals):
    list = ''
    num = 1
    for i in animals:
        list += str(num) + '. ' + i + '\n'
        num += 1
    return list
print(list_animals("Big"))