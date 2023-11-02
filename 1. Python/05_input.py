firstPerson = input("Enter the first Person Name")
ageOfFirstPerson = int(input("Enter Your Age ? "))
secondPerson = input("Enter the Second Person Name")
ageOfSecondPerson = int(input("Enter Your Age ? "))
if ageOfFirstPerson > ageOfSecondPerson:
    print(firstPerson, "is older than", secondPerson)
else:
    print(secondPerson, "is older than", firstPerson)