import os
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/workarea1', methods=['GET','POST'])
def workarea1():
    if request.method == 'POST':
        print 'entering processing'
        print request.form['firstname']
        print request.form['lastname']
        args = []
        args.append(request.form['firstname'])
        args.append(request.form['lastname'])
        for arg in args:
            print arg
        return render_template('workarea1.html', args=args)
    else:
        return render_template('workarea1.html')

@app.route('/imageproc')
def imageproc():
    return render_template('imageproc.html')


if __name__ == "__main__":
    app.run(debug=True);
