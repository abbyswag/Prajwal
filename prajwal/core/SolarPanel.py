from PVCell import PVCell

class SolarPanel:
    """Solar Panel Class"""
    def __init__(self,ratedPower,ratedEfficiency,area,cellCount,nominalCellTemp,tempCofficient = -0.005):
        """ratedPower - watts
            ratedEfficiency - %
            area - m^2
            cellCount - number
            nominalCellTemp - *C """
        self.cellCount = cellCount
        self.area = area
        self.cell = PVCell(ratedPower/cellCount,ratedEfficiency/100,nominalCellTemp,tempCofficient)

    def getElectricPower(self,ambidentTemp,radiation):
        return self.cell.getElectricPower(ambidentTemp,radiation,self.area)*self.cellCount


