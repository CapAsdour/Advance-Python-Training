from statistics import mean
from scipy import stats
import matplotlib.pyplot as plt
Estimates = [1000,1010,1786,2000,1500,1500,100,120,150,
             150,150,170,175,180,197,200,200,200,200,200,
             200,220,220,220,220,234,250,250,250,250,250,
             250,250,250,250,263,270,275,275,286,300,300,
             300,300,300,300,300,300,320,350,350,350,400,
             400,400,400,400,450,467,500,500,500,500,500,
             500,500,550,550,600,600,600,650,700,700,720]
trim_val=int(0.1*len(Estimates))
Estimates.sort()
'''
scipy provides the stats librart which has trim mean function 

'''
m=stats.trim_mean(Estimates,0.1)
print(m)
'''
Estimates=Estimates[trim_val:]
Estimates=Estimates[:len(Estimates)-trim_val]
print(mean(Estimates))
'''
y=[]
for i in range(len(Estimates)):
    y.append(65)
    
plt.plot(Estimates,y, 'bs')
plt.plot(m,67,'ro')