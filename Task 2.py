#Task 1

coachcosts = 550
ticket = 30
student = int(input("How many students?"))
while student > 45 or student < 0:
    print("Invalid")
    student = int(input("How many students?"))

if student > 10:
    costs = coachcosts + ticket *(student - student//10)
    print("This is your costs: $",costs)

else:
    costs = coachcosts + student * ticket
    print("This is your costs: $",costs)

recommended = costs/student * 1.05
print("Recommended costs each students: $", recommended )
print("--------------------------------------------------")

Studentnames = []
paids = []

#Task 2


while student > 45 or student < 0:
    print("Invalid!")
    student = int(input("How many students?"))
    
    
for i in range (student):
    names = input("What is your name?")
    paid = input("Have you paid?")
    while paid != "Y" and paid != "y" and paid != "N" and paid != "n":
        paid = input("Have you paid?")
        
    Studentnames.append(names)
    paids.append(paid)

print("--------------------------------------------------")
paidcount = 0
print("Students who paid:")
for l in range(len(paids)):
        if paids[l] == "y" or  paids[l] == "Y":
            print(Studentnames[l],paids[l])
            paidcount = paidcount + 1

print("Students who haven't paid:")


for m in range(len(paids)):
    if paids[m] == "n" or paids[m] == "N":
            print(Studentnames[m], paids[m])
print("--------------------------------------------------")            

#Task 3          
income = paidcount* (recommended)
print("This is your income:",income)


totalprofit = income - costs

if totalprofit > 0:
    print("You have made a profit of:", totalprofit)
elif totalprofit == 0:
    print("You have broke even.")
else:
    print("You have made a loss of:", totalprofit)

