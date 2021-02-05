import json
import urllib.request
from prajwal.core.solarPanel import SolarPanel

panel = 'panel'
radiation = 1000
panelCount = 1
lat = 20.8
lon = 80.9

def setLocation(lat,lon):
    lat = lat
    lon = lon

def setRadiation(radiation):
    radiation = radiation

def createPanel(ratedPower,ratedEfficiency,nominalCellTemp,panelArea,cellCount,panelCount):
    panelCount = panelCount
    panel = SolarPanel(float(ratedPower),float(ratedEfficiency),float(nominalCellTemp),float(panelArea),int(cellCount))

def loadApiKey():
    try:
        with open('apiKey.txt','r') as f:
            key = f.readline()
    except:
        key = '746f6fd0c9a7640e6f07eca2eff86c71'
    return key

def fetchTemp(self,lat,lon):
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat='+str(lat)+'&lon='+str(lon)+'&exclude={part}&appid='+loadApiKey()
    with urllib.request.urlopen(url) as f:
        data = json.load(f)
        temp = float(data['current']['temp'])
    return temp-273

def getElectricPower(temp):
    panel.getElectricPower(temp,radiation)*panelCount

def getEfficiency(temp):
    panel.getEfficiency(temp,radiation)

def getOutput():
    temp = fetchTemp(lat,lon)
    return {
        'electric-power':getElectricPower(temp),
        'efficiency':getEfficiency(temp)
    }