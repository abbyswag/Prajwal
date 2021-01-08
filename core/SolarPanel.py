class SolarPanel:
    def __init__(self,efficiency,area)
        self.efficiency = efficiency
        self.area = area

    def getEnergyOutput(self,input = 1000):
        return self.efficiency*self.area*input

    def getEfficiency(self):
        return self.efficiency