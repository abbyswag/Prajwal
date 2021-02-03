import os
from flask import request, render_template
from werkzeug.utils import secure_filename

def mainRoute(app):

    @app.route('/paneldata', methods = ['POST'])
    def getPanelData():
        if request.method == 'POST':
            ratedPower = request.form['rated-power']
            ratedEfficiency = request.form['rated-efficiency']
            nominalCellTemp = request.form['nominal-cell-temp']
            panelArea = request.form['panel-area']
            panelCount = request.form['panel-count']
            cellCount = request.form['cell-count']
        return render_template('enviroment.html')


    uploads = os.path.join(app.instance_path, 'uploads')

    @app.route('/enviromentdata', methods = ['POST','GET'])
    def getEnviroData():
        if request.method == 'POST':
            radiation = request.form['radiation']
            ambidentTemp = request.form['ambident-temp']
            envImage = request.files['image']
            envImage.save(uploads + '/' + secure_filename(envImage.filename))
        return render_template('output.html')