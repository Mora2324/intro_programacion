names = ["Daniel", "Alexix", "Violeta", "Victor", "Manuel"]

print("La lista tiene", len(names), "elementos")
print(names[1])
print(names[-1])

for elements in names:
    if elements[0] == "V":
        print(elements)
