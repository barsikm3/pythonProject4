cellphones = ["Nokia.lpp", "Apple.sst", "Samsung.lpp", "Ericson.mt"]
oldi = []
for phones in cellphones:
    if phones.endswith(".lpp"):
        phones = phones.replace(".lpp", "I will get it soon")
        oldi.append(phones)
    else:
        oldi.append(phones)
print(oldi)
