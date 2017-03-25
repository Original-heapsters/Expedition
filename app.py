import os
import json
import requests
from havenondemand.hodclient import *
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


app = Flask(__name__)
UPLOAD_FOLDER = './static/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'])
hpe_key = '4c79bcc2-72f4-41db-9f07-4552174c8cc1'
hodClient = HODClient(hpe_key)
hpe_anomaly = 'https://api.havenondemand.com/1/api/sync/anomalydetection/v1?apikey='+hpe_key

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/workarea1', methods=['GET','POST'])
def workarea1():
    if request.method == 'POST':

        if 'file' in request.files:
            print 'found file'
            file = request.files['file']

            if file.filename is not '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.abspath(app.config['UPLOAD_FOLDER'] + filename))
                param_arr = {}
                param_arr["file"] = app.config['UPLOAD_FOLDER'] + filename

                r = hodClient.post_request(param_arr, 'anomalydetection', async=False)
                anomaly = json.dumps(r)

                r = hodClient.post_request(param_arr, 'trendanalysis', async=False)
                trend = json.dumps(r)


                r= hodClient.post_request(param_arr, 'predict', async=False)
                predict = json.dumps(r)

        args = []
        args.append(request.form['firstname'])
        args.append(request.form['lastname'])
        return render_template('workarea1.html', args=args,anomaly=anomaly, trend=trend, predict=predict)
    else:
        return render_template('workarea1.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/imageproc')
def imageproc():
    return render_template('imageproc.html')


if __name__ == "__main__":
    app.run(debug=True);
