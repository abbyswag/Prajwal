import matplotlib.pyplot as plt
from PVCell import PVCell

"""Test coditions for pv cell"""

cellLst = []
with open('PVCell_test_data.txt','r') as f:
    for line in f:
        data = list(map(float,line.split(' ')))
        cell = PVCell(data[0]*data[1],data[2]*data[3],data[4])
        cellLst.append(cell)    

"""Temprature vs cell efficiecy and temprature"""

temp = []
cellTemp,efficiecy,energy = [],[],[]
for i in range(20):
    temp.append(5*i)
    cellTemp.append(cellLst[0].getCellTemp(5*i,1))
    efficiecy.append(cellLst[0].getEfficiency(5*i,1))
    energy.append(cellLst[0].getElectricPower(5*i,1))

plt.plot(temp,cellTemp)
plt.ylabel('cell temprature')
plt.axis([0,200,0,200])
plt.show()

plt.plot(temp,efficiecy)
plt.ylabel('electrical efficiency')
plt.axis([0,100,0,1])
plt.show()

plt.plot(temp,energy)
plt.ylabel('electrical energy (Kilo Watt)')
plt.show()