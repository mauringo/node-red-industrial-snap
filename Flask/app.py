from flask import Flask, redirect, render_template, request, session, url_for, Response
from werkzeug.utils import secure_filename as a


import time
import subprocess
import os 
import sys




print("output will be redirected")
# stdout is saved


dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path+"/uploads")
app = Flask(__name__, static_url_path='')



os.chdir(dir_path)

# Uploads

@app.route('/', methods=['GET', 'POST'])
def index():
    
    
    return render_template('modify.html')

@app.route('/disableconf')
def removeFileStart():
    try:
       os.remove("./configurator.enabled")
       print("File Removed!")
    except:
       print("File not present")

    return render_template('modify.html')

@app.route('/rundefault')
def removeFile():
    try:
       os.remove("./hello.conf")
       print("File Removed!")
    except:
       print("File not present")

    return render_template('modify.html')

@app.route('/writeconf', methods=['GET', 'POST'])
def my_form():
    if request.method == 'POST':
        print("triggered")
        # write to file
        with open('./settings.js', 'w') as f:
           f.write(str(request.data.decode('UTF-8')))

    return render_template('modify.html')



@app.route('/stream')
def stream():
    def generate():
        with open('./settings.js') as f:
            a=f.read()
            f.close()
            return a
                

    return Response(generate(), mimetype='text/plain')
		
if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True, port=1882)
