from flask import Flask as flask
from flask import render_template
from flask import request
import os
app=flask(__name__)
@app.route('/')
def main():
    firname=os.listdir('static/mp')
    return render_template('main.html',firname=firname)
@app.route('/up',methods=['GET','POST'])
def up():
    if request.method == 'POST':
        file = request.files['file']
        file.save('static/mp/'+file.filename)
    return render_template('up.html')
app.run()