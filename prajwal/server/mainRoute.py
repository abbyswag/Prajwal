import os
from flask import request, render_template
from werkzeug.utils import secure_filename
from prajwal.core import createPanel,setLocation,setRadiation,getOutput

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
            
            createPanel(ratedPower,ratedEfficiency,nominalCellTemp,panelArea,cellCount,panelCount)
        return render_template('enviroment.html')


    @app.route('/location', methods = ['POST'])
    def getLocation():
        data = request.json
        location = data['location']
        lat, lon = tuple(map(float,location.split(',')))
        setLocation(lat,lon)
        return {
            'message':'location recieved'
        }
        

    @app.route('/enviromentdata', methods = ['POST','GET'])
    def getEnviroData():
        if request.method == 'POST':
            image = request.files['image']
            radiation = request.form['radiation']

            rad = round(float(radiation),4)
            setRadiation(rad)

            uploads = os.path.join(app.instance_path, 'uploads')
            image.save(uploads + '/' + secure_filename(image.filename))

        return getOutput()