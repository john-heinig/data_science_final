import matplotlib.pyplot as plt
import numpy as np 
import json

# this script takes information from current mlb teams and plots them then finds the line of best fit and
# gets the data from war.json to plot the cemeteries with that line of best fit.
y = np.array([104,100,99,101,90,90,89,90,82,87,92,88,84,82,84,83,82,75,78,76,71,79,78,76,73,71,56,61,50,59])
x = np.array([5.933333333,5.144444444,5.155555556,4.422222222,5.255555556
,4.744444444
,4.722222222
,4.422222222
,5.244444444
,4.633333333
,3.955555556
,4.2
,4.088888889
,4.077777778
,3.733333333
,3.811111111
,3.633333333
,4.233333333
,3.9
,4.111111111
,4.655555556
,3.633333333
,3.655555556
,3.277777778
,3.555555556
,2.422222222
,3.255555556
,2.444444444
,2.777777778
,1.688888889])

slope, intercept = np.polyfit(x, y, 1)

# un-comment this line to see the mlb team plot
#plt.scatter(x, y )

plt.title("Cemetery teams average war per player to wins")
plt.ylabel("Team Wins")
plt.xlabel("Average War")
#plt.plot(x, slope * x + intercept, color='red')
list = []
with open("war_test.json", "r") as f:
    list = json.load(f)
x =[]
for i in list:
    x.append(i[2])
    
x = np.array(x)

y = []
for i in x:
    y.append(slope * i + intercept)
y = np.array(y)

plt.scatter(x, y )




plt.show()