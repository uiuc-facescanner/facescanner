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

@app.route('/manip-data')
def manip_data():
	# various functions to manipulate data
	return render_template('do-something.html')
	
@app.route('/view-detected')
def view_detected():
	return render_template('view-pictures-detected.html')
	
@app.route('/view-original')
def view_original():
	return render_template('view-pictures-original.html')

if __name__ == '__main__':
	app.run(debug=True)
