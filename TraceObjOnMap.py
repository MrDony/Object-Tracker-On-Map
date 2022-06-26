import csv
import matplotlib.pyplot as plt
import numpy as np

with open('VelocityData.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

posx = [0]*len(data)
posy = [0]*len(data)
posx[1]=1.0
posy[1]=4.9

for i in range(2,len(data)):
    #plt.scatter(posx, posy)
    #plt.show()
    #print('\n')
    #print(data[i])
    l_time=str(data[i][0])
    from datetime import datetime
    pt = datetime.strptime(l_time,'%H:%M')
    #total_seconds = pt.minute*60 + pt.hour*3600
    #print(":",total_seconds,":")
    vx = float(data[i][1])
    vy = float(data[i][2])
    #print(vx," ",vy)
    posx[i]=posx[i-1]+vx
    posy[i]=posy[i-1]+vy

    
    #print(i)
    #print("px = ",posx[i]," py = ",posy[i])
    #print("vx = ",float(data[i][1])," vy = ",float(data[i][2]))

dist=0
#find the distance between starting point and ending point
#the sarting point is posx[1],posy[1] and ending point it posx[len(data)],posy[len(data)]
im = plt.imread("map.jpg")

implot = plt.imshow(im)

plt.scatter(posx,posy)
plt.ylim(-20,max(posx)+130)
plt.xlim(-20,max(posy)+50)
#plt.gca().invert_yaxis()
plt.show()



