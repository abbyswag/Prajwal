from flask import Flask
from flask import request

@app.route('/paneldata', methods = ['POST'])
def getPanelData():
    if request.method == 'POST':
        ratedPower = request.form['rated-power']
        ratedEfficiency = request.form['rated-efficiency']
        panelArea = request.form['panel-area']
        nominalCellTemp = request.form['nominal-cell-temp']

