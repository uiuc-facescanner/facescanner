#import camera
import face

import glob
import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, render_template, request, url_for, abort, render_template, flash, session, g

# from camera import camera_init, start_scanning

app = Flask(__name__)

""" TODO: Define and implement routes for

* Camera configuration
* Data analysis
* View original pictures
* View pictures with faces detected
* Logs

among other things.
"""

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/camera-start')
def camera_start():
	# start_scanning()
	return render_template('camera-start.html')

@app.route('/scan-start')
def scan_start():
	path = 'static/photos_orig/*.jpg'
	images=glob.glob(path)
	count = 0; # face counter
	print images
	for image in images:
		count += face.numfaces(image)
	return render_template('scan-start.html', count=count)

@app.route('/view-faces')
def view_faces():
	path = 'static/photos_scanned/*.jpg'
	files=glob.glob(path)
	return render_template('view-faces.html', files=files)

@app.route('/view-original')
def view_original():
		path = 'static/photos_orig/*.jpg'
		files=glob.glob(path)
		return render_template('view-pictures-original.html', files=files)

if __name__ == '__main__':
	# camera_init()
	app.run(debug=True)
