from PVCell import PVCell

class SolarPanel:
    """Solar Panel Class"""
    def __init__(self,area,ratedPower,cellCount,nocTemp,tempCofficient):
        self.cellCount = cellCount
        self.cell = PVCell(area/cellCount,ratedPower/cellCount,nocTemp,tempCofficient)

    def getElectricPower(self,temp,effectiveRadiation):
        return self.cell.getElectricPower(temp,effectiveRadiation)*self.cellCount

    def getEffectiveRadiation(self,radiation):
        pass

    def getInclinationFactor(self,angle):
        pass

    def getAltitudeFactor(self,angle):
        pass

    def getMaxPowerVoltage(self,openCircuitVoltage,shortCircuitCurrent):
        pass
