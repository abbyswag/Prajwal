"""
This is PV cell simulation based on doffie and beckman equation given in 1991. 
According to this equation solar energy that falls on the pv cell will change 
into heat energy and electrical energy.

Parameters of the equation:
solar absorbance (%)
solar transmittence (%)
solar radiation (kW/m^2)
cell temprature (C)
ambient temprature (C) 
elecrical conversion effeciency (constant)
cofficient of heat transfer (kW/m^2*C)
"""

class PVCell:
    """Photo Voltanic Cell Class"""
    def __init__(self,area,stcRatedPower,stcEfficiency,nominalCellTemp = 45,tempCofficient = -0.005):
        """ area - area of PV cell
            stcRatedPower - output power of PV cell at STC
            stcEfficiency - efficiency at STC in experiment
            nominalCellTemp - cell temprature at NOC
            tempCofficient - temprature cofficient for electrical efficiency"""
        self.area = area
        self.stcRatedPower = stcRatedPower
        self.stcEfficiency = stcEfficiency
        self.nominalCellTemp = nominalCellTemp
        self.tempCofficient = tempCofficient

        # some constants with their units
        self.stcRadiation = 1 # kW/m^2
        self.nocRadiation = 0.8 # kW/m^2
        self.stcCellTemp = 25 # C
        self.nocAmbientTemp = 20 # C    
        self.solarTransmittence = 0.9 # %
        self.solarAbsorptance = 1 # %

    def calcStcEfficiency(self):
        """Returns electrical conversion efficiency at STC condition by calculation."""
        return self.stcRatedPower/(self.area*self.stcRadiation)

    def getStcEfficiency(self):
        return self.stcEfficiency

    def calcFirstConst(self):
        """Returns constant one using nominal cell temprature."""
        return (self.nominalCellTemp - self.nocAmbientTemp)/self.nocRadiation

    def calcSecondConst(self):
        """Returns product of solar absorbtance and solar transmittence"""
        return self.solarAbsorptance*self.solarTransmittence

    def getApprCellTemp(self,ambientTemp,radiation):
        """Returns approximate cell temprature"""
        return ambientTemp + radiation*self.calcFirstConst()

    def getCellTemp(self,ambientTemp,radiation):
        """Returns calculated cell temprature"""
        numerator = ambientTemp + radiation*self.calcFirstConst()*(1- (self.calcStcEfficiency()/self.calcSecondConst())*(1 + self.tempCofficient*self.stcCellTemp))
        denominator = 1 - (radiation*self.calcFirstConst()*self.calcStcEfficiency()*self.tempCofficient/self.calcSecondConst())
        return numerator/denominator

    def getEfficiency(self,ambientTemp,radiation):
        """Returns electrical conversion efficiency at given cell temprature."""
        return self.getStcEfficiency()*(1 + self.tempCofficient*(self.getCellTemp(ambientTemp,radiation) - self.stcCellTemp))
    
    def getElectricPower(self,ambientTemp,radiation):
        """Returns output electric power."""
        return self.getEfficiency(ambientTemp,radiation)*radiation
