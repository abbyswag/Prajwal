import os
from flask import request, render_template
from werkzeug.utils import secure_filename
from prajwal.core import Handler

def dataRoute(app):
    coreHandler = Handler()

    @app.route('/data/paneldata', methods = ['POST','GET'])
    def fetchPanelData():
        if request.method == 'POST':
            try:
                ratedPower = float(request.form['rated-power'])
                ratedEfficiency = float(request.form['rated-efficiency'])
                nominalCellTemp = float(request.form['nominal-cell-temp'])
                panelArea = float(request.form['panel-area'])
                cellCount = int(request.form['cell-count'])
                panelCount = int(request.form['panel-count'])
            except:
                return render_template('data.html')
            
            coreHandler.setPanel(ratedPower,ratedEfficiency,nominalCellTemp,panelArea,cellCount,panelCount)
            return render_template('enviroment.html')
        else:
            return render_template('data.html')


    @app.route('/data/location', methods = ['POST'])
    def getLocation():
        data = request.json
        location = data['location']
        try:
            (lat,lon) = tuple(map(float,location.split(',')))
            coreHandler.setLocation(lat,lon)
        except:
            return {
                'message': 'co-ordinates are not in float'
            }
        return {
            'message':'location co-ordinates are recieved'
        }

    @app.route('/data/radiation', methods = ['POST'])
    def getRadiation():
        data = request.json
        radiation = data['radiation']
        try:
            rad = float(radiation)
            coreHandler.setRadiation(rad)
        except:
            return {
                'message': 'radiation value is not a float'
            }
        return {
            'message':'radiation value is recieved'
        }
        

    @app.route('/data/envimage', methods = ['POST','GET'])
    def getEnvImage():
        if coreHandler.getPanel() == 'panel':
            return render_template('data.html')
        else:
            if request.method == 'POST':
                image = request.files['image']
                try:
                    # saving image in envImages
                    envImages = os.path.join(app.instance_path, 'envImages')
                    image.save(envImages + '/' + secure_filename(image.filename))
                except:
                    return render_template('enviroment.html')
                return render_template('output.html')
            else:
                render_template('data.html')

    @app.route('/data/output')
    def getOutput():
        return {
            'electricPower': coreHandler.getElectricPower(),
            'efficiency' : coreHandler.getEfficiency(),
            'inclination' : 45,
            'orientation' : 'south'
        }