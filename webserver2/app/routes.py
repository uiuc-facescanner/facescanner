from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/hello', methods=['POST'])
def hello():
	info=request.form['info']
	return render_template('hello.html', info=info)

if __name__ == '__main__':
	app.run(debug=True)
