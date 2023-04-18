#Task 1
BusA=[]
BusB=[]
BusC=[]
BusD=[]
BusE=[]
BusF=[]
print("Please enter the following detail in the prder of Bus A, B, C, D, E, F")

for a in range(20):
    minutes = int(input("how many minutes lates/early? - please enter in order of the date"))
    BusA.append(minutes)
for b in range(20):
    minutes = int(input("how many minutes lates/early? - please enter in order of the date"))
    BusB.append(minutes)

for c in range(20):
    minutes = int(input("how many minutes lates/early? - please enter in order of the date"))
    BusC.append(minutes)

for d in range(20):
    minutes = int(input("how many minutes lates/early? - please enter in order of the date"))
    BusD.append(minutes)

for e in range(20):
    minutes = int(input("how many minutes lates/early? - please enter in order of the date"))
    BusE.append(minutes)

for f in range(20):
    minutes = int(input("how many minutes lates/early? - please enter in order of the date"))
    BusF.append(minutes)


print('Data (from Bus A to Bus F in ascending order):')
#First week print days
print('Monday 1:', BusA[0],BusB[0],BusC[0], BusD[0],BusE[0],BusF[0])
print('Tuesday 1:', BusA[1],BusB[1],BusC[1], BusD[1],BusE[1],BusF[1])
print('Wednesday 1:', BusA[2],BusB[2],BusC[2], BusD[2],BusE[2],BusF[2])
print('Thursday 1:', BusA[3],BusB[3],BusC[3], BusD[3],BusE[3],BusF[3])
print('Friday 1:', BusA[4],BusB[4],BusC[4], BusD[4],BusE[4],BusF[4])
#Second week print days
print('Monday 2:', BusA[5],BusB[5],BusC[5], BusD[5],BusE[5],BusF[5])
print('Tuesday 2:', BusA[6],BusB[6],BusC[6], BusD[6],BusE[6],BusF[6])
print('Wednesday 2:', BusA[7],BusB[7],BusC[7], BusD[7],BusE[7],BusF[7])
print('Thursday 2:', BusA[8],BusB[8],BusC[8], BusD[8],BusE[8],BusF[8])
print('Friday 2:', BusA[9],BusB[9],BusC[9], BusD[9],BusE[9],BusF[9])
#Third week print days
print('Monday 3:', BusA [10],BusB[10],BusC[10], BusD[10],BusE[10],BusF[10])
print('Tuesday 3:', BusA [11],BusB[11],BusC[11], BusD[11],BusE[11],BusF[11])
print('Wednesday 3:', BusA [12],BusB[12],BusC[12], BusD[12],BusE[12],BusF[12])
print('Thursday 3:', BusA [13],BusB[13],BusC[13], BusD[13],BusE[13],BusF[13])
print('Friday 3:', BusA [14],BusB[14],BusC[14], BusD[14],BusE[14],BusF[14])
#Fourth week print days
print('Monday 4:', BusA[15],BusB[15],BusC[15], BusD[15],BusE[15],BusF[15])
print('Tuesday 4:', BusA[16],BusB[16],BusC[16], BusD[16],BusE[16],BusF[16])
print('Wednesday 4:', BusA[17],BusB[17],BusC[17], BusD[17],BusE[17],BusF[17])
print('Thursday 4:', BusA[18],BusB[18],BusC[18], BusD[18],BusE[18],BusF[18])
print('Friday 4:', BusA[19],BusB[19],BusC[19], BusD[19],BusE[19],BusF[19])




print('-----------------------------------------------------------------------')
#Task 2
lateday =[]
highest = -90
late = 0
minlate = 0
averagelate = 0
for k in BusA:
    if k < 0:
        late = late + 1
        minlate = minlate + k
lateday.append(late)
average = minlate/20
if late == 0:
    averagelate ==0
else:
    
    averagelate = minlate / late
print('Bus A:\nNumber of lates:',late,'\naverage late(using every data)',average*-1, '\ntotal late minutes',
      minlate*-1,'\naverage minutes late(using only the late data',averagelate*-1)


late1 = 0
minlate1 = 0
averagelate1 =0
for m in BusB:
    if m < 0:
        late1 = late1 + 1
        minlate1 = minlate1 + m
lateday.append(late1)
average1 = minlate1/20
if late1 == 0:
    averagelate1 ==0
else:
    
    averagelate1 = minlate1 / late1

print('Bus B:\nNumber of lates:',late1,'\naverage late(using every data)',average1*-1,'\ntotal late minutes',
      minlate1*-1,'\naverage minutes late(using only the late data',averagelate1*-1)

#For Bus C
late2 = 0
minlate2 = 0
averagelate2 =0
for n in BusC:
    if n < 0:
        late2 = late2 + 1
        minlate2 = minlate2 + n
lateday.append(late2)
average2 = minlate2/20
if late2 == 0:
    averagelate2 ==0
else:
    averagelate2 = minlate2 / late2

print('Bus C:\nNumber of lates:',late2,'\naverage late(using every data)',average2*-1,'\ntotal late minutes',
      minlate2*-1,'\naverage minutes late(using only the late data',averagelate2*-1)

#For Bus D
late3 = 0
minlate3 = 0
averagelate3 =0
for f in BusD:
    if f < 0:
        late3 = late3 + 1
        minlate3 = minlate3 + f
lateday.append(late3)
average3 = minlate3/20
if late3 == 0:
    averagelate3 ==0
else:
    averagelate3 = minlate3 / late3

print('Bus D:\nNumber of lates:',late3,'\naverage late(using every data)',average3*-1,'\ntotal late minutes',
      minlate3*-1,'\naverage minutes late(using only the late data',averagelate3*-1)
#For Bus E

late4 = 0
minlate4 = 0
averagelate4 =0
for g in BusE:
    if g < 0:
        late4 = late4 + 1
        minlate4 = minlate4 + g
lateday.append(late4)
average4 = minlate4/20
if late4 == 0:
    averagelate4 ==0
else:
    averagelate4 = minlate4 / late4

print('Bus E:\nNumber of lates:',late4,'\naverage late(using every data)',average4*-1, '\ntotal late minutes',
      minlate4*-1,'\naverage minutes late(using only the late data',averagelate4*-1)

#For Bus F

late5 = 0
minlate5 = 0
averagelate5 =0
for h in BusF:
    if h < 0:
        late5 = late5 + 1
        minlate5 = minlate5 + h
lateday.append(late5)
average5 = minlate5/20
if late5 == 0:
    averagelate5 ==0
else:
    averagelate5 = minlate5 / late5

print('Bus F:\nNumber of lates:',late5,'\naverage late(using every data)',average5*-1, '\ntotal late minutes',
      minlate5*-1,'\naverage minutes late(using only the late data',averagelate5*-1)

#Finding the highest
for h in lateday:
    if h > highest:
        highest = h
if lateday[0] == highest:
    print('Bus A has the highest number of late stops')
if lateday[1] == highest:
    print('Bus B has the highest number of late stops')
if lateday[2] == highest:
    print('Bus C has the highest number of late stops')
if lateday[3] == highest:
    print('Bus D has the highest number of late stops')
if lateday[4] == highest:
    print('Bus E has the highest number of late stops')
if lateday[5] == highest:
    print('Bus F has the highest number of late stops')

#Task 3
date = ["Mon1", "Tue1", 'Wed1','Thurs1','Fri1',"Mon2", "Tue2", 'Wed2','Thurs2','Fri2',"Mon3", "Tue3", 'Wed3','Thurs3','Fri3',"Mon4", "Tue4", 'Wed4','Thurs4','Fri4']
Daysss = []
print('------------------------------------------------------------------')
day = input("Which day do you want to look at the bus report?")

dayA = BusA[date.index(day)]
dayB = BusB[date.index(day)]
dayC = BusC[date.index(day)]
dayD = BusD[date.index(day)]
dayE = BusE[date.index(day)]
dayF = BusF[date.index(day)]
Daysss.append(dayA)
Daysss.append(dayB)
Daysss.append(dayC)
Daysss.append(dayD)
Daysss.append(dayE)
Daysss.append(dayF)
print(Daysss)

latemin = []
Latebuses = []
countlatebus = 0
for d in Daysss:
    if d < 0:
        countlatebus = countlatebus + 1
        if Daysss.index(d) == 0:
            Latebuses.append("Bus A")
            latemin.append(d)
        if Daysss.index(d) == 1:
            Latebuses.append("Bus B")
            latemin.append(d)
        if Daysss.index(d) == 2:
            Latebuses.append("Bus C")
            latemin.append(d)
        if Daysss.index(d) == 3:
            Latebuses.append("Bus D")
            latemin.append(d)
        if Daysss.index(d) == 4:
            Latebuses.append("Bus E")
            latemin.append(d)
        if Daysss.index(d) == 5:
            Latebuses.append("Bus F")
            latemin.append(d)
        
print('number of buses that are late:', countlatebus)

for a in range(len(latemin)):
    print(Latebuses[a],"Late", "by", latemin[a]*-1, "minutes")
    






