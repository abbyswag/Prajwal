import os
from flask import request, render_template
from werkzeug.utils import secure_filename
from prajwal.core import Handler

def mainRoute(app):
    coreHandler = Handler()

    @app.route('/paneldata', methods = ['POST','GET'])
    def fetchPanelData():
        if request.method == 'POST':
            ratedPower = request.form['rated-power']
            ratedEfficiency = request.form['rated-efficiency']
            nominalCellTemp = request.form['nominal-cell-temp']
            panelArea = request.form['panel-area']
            cellCount = request.form['cell-count']
            panelCount = request.form['panel-count']

            coreHandler.setPanel(ratedPower,ratedEfficiency,nominalCellTemp,panelArea,cellCount,panelCount)
        return render_template('enviroment.html')


    @app.route('/location', methods = ['POST'])
    def getLocation():
        data = request.json
        location = data['location']
        (lat,lon) = tuple(map(float,location.split(',')))

        coreHandler.setLocation(lat,lon)
        return {
            'message':'location recieved'
        }

    @app.route('/radiation', methods = ['POST'])
    def getRadiation():
        data = request.json
        radiation = data['radiation']
        rad = round(float(radiation),4)

        coreHandler.setRadiation(rad)
        return {
            'message':'radiation recieved'
        }
        

    @app.route('/enviromentimg', methods = ['POST','GET'])
    def getEnviromentImg():
        if request.method == 'POST':
            image = request.files['image']
            
            uploads = os.path.join(app.instance_path, 'uploads')
            image.save(uploads + '/' + secure_filename(image.filename))
        return coreHandler.getOutput()