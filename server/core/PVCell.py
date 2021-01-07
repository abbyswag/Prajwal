class PVCell:
    """Photo Voltanic Cell Class"""
    # some constants
    stcRadiation = 1000
    ntocRadiation = 800
    stcCellTemp = 298
    ntocAmbientTemp = 293
    solarTransmittence = 1 # random value
    solarTransmittence = 1 # random value

    def __init__(self,area,ratedPower,nominalCellTemp,tempCofficient):
        self.area = area
        self.ratedPower = ratedPower
        self.nominalCellTemp = nominalCellTemp
        self.tempCofficient = tempCofficient

    def getStdEfficiency(self):
        """Returns electrical conversion efficiency at STC condition."""
        return self.ratedPower/(self.area*stcRadiation)

    def getCellTemp(self):
        pass

    def getEfficiency(self,celltemp):
        """Returns electrical conversion efficiency at given temprature."""
        return self.getStdEfficiency()*(1 + self.tempCofficient*(celltemp - stcCellTemp))
    
    def calcFirstConst(self):
        """Returns a constant of energy balance equation."""
        return (self.nominalCellTemp - ntocAmbientTemp)/ntocRadiation

    def calcSecondConst(self):
        """Returns anothor constant"""
        return solarAbsorptance*solarTransmittence
    
    def getElectricPower(self,temp,radiation):
        """Returns output electric power."""
        e = self.getStdEfficiency()
        n = 1 + self.tempCofficient*(temp - stcCellTemp + self.calcFirstConst()*radiation)
        d = 1 + self.tempCofficient*(e*radiation*self.calcFirstConst()/self.calcSecondConst())
        return e*n/d
