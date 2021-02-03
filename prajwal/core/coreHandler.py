import urllib.request
import json
from solarPanel import SolarPanel

class CoreHandler:
    def __init__(self):
        pass

    # setters

    def setRadiation(self,radiation):
        self.radiation = radiation
    
    def setLatLon(self,lat,lon):
        self.lat = lat
        self.lon = lon

    def setEnviroment(self,radiation,lat,lon):
        self.setRadiation(radiation)
        self.setLatLon(lat,lon)
        
    def setPanel(self,ratedPower,ratedEfficiency,nocTemp,panelArea,cellCount,panelCount):
        self.panel = SolarPanel(ratedPower,ratedEfficiency,panelArea,cellCount,nocTemp)
        self.panelCount = panelCount

    # api implementation for finding temp

    def loadApiKey(self):
        with open('apiKey.txt','r') as f:
            key = f.readline()
        return key
    
    def fetchTemp(self,lat,lon):
        url = 'https://api.openweathermap.org/data/2.5/onecall?lat='+str(lat)+'&lon='+str(lon)+'&exclude={part}&appid='+self.loadApiKey()
        with urllib.request.urlopen(url) as f:
            data = json.load(f)
            temp = float(data['current']['temp'])
        return temp-273

    # getters
    
    def getElectricPower(self,temp):
        return self.panel.getElectricPower(temp,self.radiation)*self.panelCount
    
    def getEfficiency(self):
        return panel.getEfficiency(temp,self.radiation)

    def getOutput(self):
        temp = self.fetchTemp(self.lat,self.lon)
        return {
            'electric-power':self.getElectricPower(temp),
            'efficiency':self.getEfficiency(temp)
        }
        