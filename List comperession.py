list = []
for x in range(1,22):
    list.append(x*7)
print(list)
list2 = [ x*4 for x in range(1,35)]
print(list2)

cars = ["BMW", "AUDI", "VW", "Lamborgini", "Renault"]
lenght = [len(cars) for car in cars]
print(lenght)
v = [x for x in range(1,200) if x % 3 == 0]
print(v)

def odd_numbers(n):
    return [x for x in range(0, n+1) if x%2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
