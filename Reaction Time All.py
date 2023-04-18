#Task1
ages = []
houses=[]
reactiontime = []
for i in range(4):
    age = int(input('how old?'))
    while age < 12 or age > 16:
       print('Age should be in the correct range.')
       age = int(input('how old?')) 
    house = input('which house?')
    while house != 'Saturn' and house != 'Mars':
        print('Sorry, this is not one of our houses')
        house = input('which house?')
    reaction = int(input('what is the reaction time?'))
    
    ages.append(age)
    houses.append(house)
    reactiontime.append(reaction)
    
#Task2
count = 0
time = 0
countmars = 0
timemar = 0
for m in range(len(houses)):
    if houses[m] == 'Saturn':
        count = count + 1
        time = time + reactiontime[m]
    else:
        countmars = countmars +1
        timemar = timemar + reactiontime[m]

average = time/count
averagemar=timemar/countmars
print('the reaction time average of Saturn',average)
print('the reaction time average of Mars:',averagemar)
print('---------------------------------------------')

#Task3
countpart = 0
reactpart =0
lowest = 100000
reactlist=[]
ageask = int(input('what age want to see?'))
while ageask < 12 or ageask > 16:
       print('Age should be in the correct range.')
       ageask = int(input('what age want to see?'))
houseask = input ('which house in?')
while houseask != 'Saturn' and houseask != 'Mars':
        print('Sorry, this is not one of our houses')
        houseask = input ('which house in?')
print('---------------------------------------------')

for b in range(len(ages)):
    if ages[b] == ageask:
        if houses[b] == houseask:
            reactpart = reactpart + reactiontime[b]
            reactlist.append(reactiontime[b])
            countpart = countpart + 1
print('average of them:',reactpart/countpart)

for k in reactlist:
    if k < lowest:
        lowest = k
print('lowest reaction time:',lowest)
        
    

