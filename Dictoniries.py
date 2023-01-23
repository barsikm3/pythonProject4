dictoniries = {}
print(type(dictoniries))
files = {"txt": 10, "reb": 13, "vic": 15, "lbs": 23}
print(files)
print(files["txt"])
print(files["vic"])
print("reb" in files)
files["vic"] = 105
print(files)
del files["lbs"]
print(files)

dic = {"Argentina": 1, "France": 2, "Spain": 3, "Brazil": 4}
for teams in dic:
    print(teams)
for teams, position in dic.items():
    print("These teams {} taken all better places {}".format(position, teams))
print(dic.keys())
print(dic.values())

def count(letter):
    dic = {}
    for symb in letter:
        if letter not in dic:
            dic[letter] = 0
            dic[letter] += 1
        return dic
    print(count("bbbbbennsd"))

milk = {"Babusko": 4, "Vanuska": 23, "Lampadushka": 25}
for extension in milk:
    print(extension)

for extension, li in milk.items():
    print("That is {} in their index {}".format(li,extension))

print(milk.keys)
print(milk.values)

for li in milk.values():
    print(milk)

def count(letter):
    dic = {}
    for symb in letter:
        if letter not in dic:
            dic[symb] = 0
            dic[symb] += 1
        return dic

print(count("aaaaaaaa"))
print(count("A long string with a lot of letters"))
