def Camel(s):
    new_string = ""
    for letter in s:
        if letter.isupper():
            new_string +=" "+letter
        else:
            new_string += letter
    return new_string
print(Camel("laBudo camelLatudo"))

def mult(number):
    if number == 0:
        return None
    elif number % 3 == 0:
        return number
    else:
        return mult(number // 10)
print(mult(46))

x = ["Alex", "Lemouraa", "Ivan", "Laba", "Lita", "Pacita", "El mundo", "Varb"]
def friends(x):
    return [a for a in x if len(a) == 4]
print(friends(x))

y = ["Alex", "Lemouraa", "Ivan", "Laba", "Lita", "Pacita", "El mundo", "Varb"]
def frid(y):
    new = []
    for name in y:
        if len(name) == 4:
            new.append(name)
    return new
print(frid(y))

pets = ["humanYears", "catYears", "dogYears"]
def p(human_years):
    catYears = 0
    dogYears = 0
    if human_years == 1:
        catYears += 15
        dogYears += 15
    elif human_years == 2:
        catYears += 24
        dogYears += 24
    elif human_years >= 3:
        years = human_years - 2
        catYears += years * 4 + 24
        dogYears += years * 5 + 24
    return [human_years, catYears, dogYears]
    return [0,0,0]
print(p(10))

num = 42
print(str(num))



