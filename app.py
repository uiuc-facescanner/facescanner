#import camera
import face
import glob
from flask import Flask, render_template, request, url_for, abort, render_template, flash, session, g
import os
from sqlite3 import dbapi2 as sqlite3

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

@app.route('/camera-start')
def camera_start():
	# start_scanning()
	return render_template('camera-start.html')

@app.route('/scan-start')
def scan_start():
	count=face.numfaces()
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

# face database
# Load default config and override config from an environment variable
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'face.db'),
	DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))
app.config.from_envvar('RESTORAN_SETTINGS', silent=True)

def connect_db():
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

@app.route('/init_db')
def init_db():
	db = get_db()
	with app.open_resource('schema.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()
	return render_template('new-db.html')

@app.cli.command('initdb')
def initdb_command():
	init_db()
	print('Initialized the database.')

def get_db():
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()


# end face database

if __name__ == '__main__':
	# camera_init()
	app.run(debug=True)
