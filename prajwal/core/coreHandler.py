import urllib.request
import json
from prajwal.core.solarPanel import SolarPanel

class CoreHandler:
    def __init__(self):
        self.panel = 'panel'
        self.panelCount = 1
        self.radiation = 1000
        self.lat = 27
        self.lon = 81

    # setters
    def setPanel(self,ratedPower,ratedEfficiency,nocTemp,panelArea,cellCount,panelCount):
        self.panel = SolarPanel(float(ratedPower),float(ratedEfficiency),float(nocTemp),float(panelArea),int(cellCount))
        self.panelCount = int(panelCount)

    def setRadiation(self,radiation):
        self.radiation = float(radiation)
    
    def setLocation(self,lat,lon):
        self.lat = float(lat)
        self.lon = float(lon)

    def setEnviroment(self,radiation,lat,lon):
        self.setRadiation(radiation)
        self.setLocation(lat,lon)
        
    def panelDataValidation(self,ratedPower,ratedEfficiency,nocTemp,panelArea,cellCount,panelCount):
        if type(ratedPower) != float or type(ratedPower) != int:
            raise ValueError('ratedPower in not a number')

        
    # api implementation for finding temp

    def loadApiKey(self):
        try:
            with open('apiKey.txt','r') as f:
                key = f.readline()
        except:
            key = '746f6fd0c9a7640e6f07eca2eff86c71'
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
    
    def getEfficiency(self,temp):
        return self.panel.getEfficiency(temp,self.radiation)

    def getOutput(self):
        temp = self.fetchTemp(self.lat,self.lon)
        return {
            'electric-power':self.getElectricPower(temp),
            'efficiency':self.getEfficiency(temp)
        }