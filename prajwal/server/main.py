import os

from flask import request
from werkzeug.utils import secure_filename

from app.core.PVCell import PVCell

def mainRoute(app):

    @app.route('/paneldata', methods = ['POST'])
    def getPanelData():
        if request.method == 'POST':
            ratedPower = request.form['rated-power']
            ratedEfficiency = request.form['rated-efficiency']
            nominalCellTemp = request.form['nominal-cell-temp']
            panelArea = request.form['panel-area']
            cell = PVCell(panelArea,ratedPower,ratedEfficiency,nominalCellTemp)
        return {
            'message':'Panel data are submitted'    
        }

    uploads = os.path.join(app.instance_path, 'uploads')

    @app.route('/enviromentdata', methods = ['POST'])
    def getEnviroData():
        if request.method == 'POST':
            radiation = request.form['radiation']
            envImage = request.files['env-image']
            envImage.save(uploads + '/' + secure_filename(envImage.filename))
        return {
            'message':'Enviroment data are recieved'    
        }
