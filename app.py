#import camera
#import face
from flask import Flask, render_template, request, url_for

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
	
@app.route('/camera-start')
def camera_start():
	# function to start camera
	return render_template('camera-start.html')

@app.route('/scan-start')
def scan_start():
	#numfaces()
	return render_template('scan-start.html')
	
@app.route('/view-faces')
def view_faces():
	return render_template('view-faces.html')
	
@app.route('/view-original')
def view_original():
	return render_template('view-pictures-original.html')

if __name__ == '__main__':
	app.run(debug=True)
