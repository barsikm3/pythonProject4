animals = ["Lion", "Tiger", "Dolphin", "Rabbit"]
chars = 0
for animal in animals:
    chars += len(animal)
print("Total characters: {}, Average chars: {}".format(chars, chars/len(animals)))

team = ["Siarhei", "Alex", "Daria", "Victor"]
for index,person in enumerate(team):
    print("{} - {}".format(index +1, person))

def list_customer(people):
    list = []
    for email, name in people:
        list.append("{} - {}".format(name, email))
        return list
    print(list_customer([("s_pasiukevich@lesta.group", "Siarhei Pasiukevich")]))
    print(list_customer([("s_pasiu", "Vasia")]))


def skip_elements(elements):
    # code goes here
    new_list = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            new_list.append(element)

    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']

def skip_sheet(peace_of_sheet):
    new1_list = []
    for index, sheety in enumerate(peace_of_sheet):
        if index % 2 == 0:
            new1_list.append(sheety)
            return new1_list
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_sheet(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']