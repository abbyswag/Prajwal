import os
from flask import request, render_template
from werkzeug.utils import secure_filename
from prajwal.core.coreHandler import CoreHandler

handler = CoreHandler()

def mainRoute(app):

    @app.route('/paneldata', methods = ['POST','GET'])
    def fetchPanelData():
        if request.method == 'POST':
            ratedPower = request.form['rated-power']
            ratedEfficiency = request.form['rated-efficiency']
            nominalCellTemp = request.form['nominal-cell-temp']
            panelArea = request.form['panel-area']
            cellCount = request.form['cell-count']
            panelCount = request.form['panel-count']
            
            handler.setPanel(ratedPower,ratedEfficiency,nominalCellTemp,panelArea,cellCount,panelCount)

        return render_template('enviroment.html')


    @app.route('/enviromentdata', methods = ['POST','GET'])
    def getEnviroData():
        if request.method == 'POST':
            radiation = request.form['radiation']
            location = request.form['location']
            image = request.files['image']

            lat, lon = tuple(map(float,location.split(',')))
            rad = round(float(radiation),4)
            handler.setEnviroment(rad,lat,lon)

            uploads = os.path.join(app.instance_path, 'uploads')
            image.save(uploads + '/' + secure_filename(image.filename))

        return handler.getOutput() 