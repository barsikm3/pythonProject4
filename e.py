class VW:
    competation = ""
    name = ""
    cost = ""
    fuel = ""
    def vw_service(self):
        print("The service of VW {} {} interval is 15,000 km, and it's cost is {}, and it's fuel consumptions is {}".format(self.competation, self.name, self.cost, self.fuel))
vw_jetta = VW()
vw_jetta.name = "Jetta"
vw_jetta.cost = "19000"
vw_jetta.fuel = "8 liters"
vw_jetta.vw_service()

vw_toareg = VW()
vw_toareg.competation = "Exlusive"
vw_toareg.name = "Toarge"
vw_toareg.cost = "40000"
vw_toareg.fuel = "21 liter"
vw_toareg.vw_service()

class Points:
    win = 3
    draw = 1
    lose = 0
    def countresult(self):
        return self.win*3 + self.draw*1 + self.lose
team_result = Points()
team_result.win = 12
team_result.draw = 9
team_result.lose = 4

print(team_result.countresult())

class Apple:
    def __init__(self, devices, tablets, big_dev):
        self.devices = devices
        self.tablets = tablets
        self.big_dev = big_dev

buyinng = Apple("Iphone 11","Air 2","Macbook Air")
print(buyinng.devices, buyinng.tablets, buyinng.big_dev)

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {} and my second name is {}".format(self.name, self.surname)
some_person = Person("Siarhei", "Pasiukevich")
print(some_person.greeting())

help(Person)

class Cost_shoes:
    def __init__(self, pln, usd, byn, deliviring):
        self.pln = pln
        self.usd = usd
        self.byn = byn
        self.delivering = deliviring
    def calculating(self):
        self.usd = round(self.pln/4.44)
        self.byn = round(self.pln/1.7)
        self.delivering = self.usd + 25
        return print("The cost in PLN is: {}, in USD is: {}, in BYN is {} and the final cost is: {} USD".format(self.pln, self.usd, self.byn, self.delivering))
shoes = Cost_shoes(429, 0, 0, 0)
shoes.calculating()





class Clothing:
    material = ""

    def __init__(self, name):
        self.name = name

    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
        if item == material:
            count += Clothing.stock['amount'][n]
            n += 1
    return count

    class shirt(Clothing):
        material = "Cotton"

    class pants(Clothing):
        material = "Cotton"

    polo = shirt("Polo")
    sweatpants = pants("Sweatpants")
    polo.add_item(polo.name, polo.material, 4)
    sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
    current_stock = polo.Stock_by_Material("Cotton")
    print(current_stock)

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

class Turtle(Animal):
        category = "reptile"

        def __str__(self):
            return "I'm {} and I'm a {}!".format(name, category)

print(Turtle.category)


class Snake(Animal):
    category = "reptile"

    def __str__(self):
        return "I'm {} and I'm a {}!".format(name, category)


class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result


zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category



