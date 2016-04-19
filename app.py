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
	
@app.route('/program', methods=['POST'])
def program():
	req=request.form['info']
	if req == 'manip data':
		# Some function to manipulate or view certain data from database
		return render_template('do_something.html')
	elif req == 'original pictures':
		return render_template('view_pictures_original.html')
	elif req == 'detected pictures':
		return render_template('view_pictures_detected.html')
	elif req == 'start camera':
		# Some function here to start the camera
		return render_template('camera_start.html')
	else:
		return render_template('do_something.html')

if __name__ == '__main__':
	app.run(debug=True)
