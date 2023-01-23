import random
print(random.randint(1,10))
import datetime
print(datetime.datetime.now())
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now - datetime.timedelta(days=13525))

list = ["Vania", "Dimon", "Lexi", "Tamara", "Katerina", "Vasiliy", "Wing", "Itan", "Serg"]
print(sorted(list, key=len))
list.sort()
print(list)
