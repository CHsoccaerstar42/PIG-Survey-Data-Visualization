from matplotlib import pyplot as plt

gpa = [95, 95, 95, 95, 95, 95, 95, 91.7, 91.7, 93.3, 95, 93, 95, 86, 95,
       91.7, 91, 90.8, 85, 91.7, 95, 81.7,
       91.7, 83.3, 93.3, 91.7, 95, 95, 95, 91.7, 95, 90, 95, 95,
       95, 93.3, 95, 93.3, 90, 93.3, 95, 90, 90, 95, 95, 90, 93, 93,
       90, 95, 93.3]

sat = [1390, 1250, 1420, 1490, 1470, 1420, 1520, 1310, 1260, 1450, 1500,
       1390, 1460, 1430, 1530, 1320, 1260, 1210, 1200,
       1210, 1170, 1050, 1220, 1390, 1440, 1420, 1540, 1530,
       1560, 1490, 1240, 1270, 1000, 1270, 1450, 1360, 1140, 1280,
       1230, 1290, 1270, 1210, 1160, 1270, 1370, 
       1140, 1260, 1210, 1100, 1300,
       1230]

eightyOnePointSeven = []
eightyThreePointThree = []
eightyFive = []
eightySix = []
ninety = []
ninetyPointEight = []
ninetyOne = []
ninetyOnePointSeven = []
ninetyThree = []
ninetyThreePointThree = []
ninetyFive = []

gpas = [81.7, 83.3, 85, 86, 90, 90.8, 91, 91.7, 93, 93.3, 95]
for i in range(len(gpa)):
    if gpa[i] == 81.7:
        eightyOnePointSeven.append(sat[i])
    elif gpa[i] == 83.3:
        eightyThreePointThree.append(sat[i])
    elif gpa[i] == 85:
        eightyFive.append(sat[i])
    elif gpa[i] == 86:
        eightySix.append(sat[i])
    elif gpa[i] == 90:
        ninety.append(sat[i])
    elif gpa[i] == 90.8:
        ninetyPointEight.append(sat[i])
    elif gpa[i] == 91:
        ninetyOne.append(sat[i])
    elif gpa[i] == 91.7:
        ninetyOnePointSeven.append(sat[i])
    elif gpa[i] == 93:
        ninetyThree.append(sat[i])
    elif gpa[i] == 93.3:
        ninetyThreePointThree.append(sat[i])
    elif gpa[i] == 95:
        ninetyFive.append(sat[i])
    else:
        print('This should not be seen')
        print(gpa[i])
Sum = 0

for term in eightyThreePointThree:
    Sum += term
eightyThreePointThreeAverage = Sum / len(eightyThreePointThree)

Sum = 0

for term in eightyOnePointSeven:
    Sum += term
eightyOnePointSevenAverage = Sum / len(eightyOnePointSeven)

Sum = 0

for term in eightyFive:
    Sum += term
eightyFiveAverage = Sum / len(eightyFive)
Sum = 0

for term in eightySix:
    Sum += term
eightySixAverage = Sum / len(eightySix)
Sum = 0

for term in ninety:
    Sum += term
ninetyAverage = Sum / len(ninety)
Sum = 0

for term in ninetyPointEight:
    Sum += term
ninetyPointEightAverage = Sum / len(ninetyPointEight)
Sum = 0

for term in ninetyOne:
    Sum += term
ninetyOneAverage = Sum / len(ninetyOne)
Sum = 0

for term in ninetyOnePointSeven:
    Sum += term
ninetyOnePointSevenAverage = Sum / len(ninetyOnePointSeven)
Sum = 0

for term in ninetyThree:
    Sum += term
ninetyThreeAverage = Sum / len(ninetyThree)
Sum = 0

for term in ninetyThreePointThree:
    Sum += term
ninetyThreePointThreeAverage = Sum / len(ninetyThreePointThree)
Sum = 0

for term in ninetyFive:
    Sum += term
ninetyFiveAverage = Sum / len(ninetyFive)




averageSat = [eightyOnePointSevenAverage, eightyThreePointThreeAverage,
              eightyFiveAverage, eightySixAverage, ninetyAverage, ninetyPointEightAverage, ninetyOneAverage,
              ninetyOnePointSevenAverage, ninetyThreeAverage, ninetyThreePointThreeAverage,
              ninetyFiveAverage]

plt.plot(gpas, averageSat)
plt.title('Average SAT score at each recorded GPA')
plt.show()




