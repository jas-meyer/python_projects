from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app.
app = Flask(__name__)   
app.secret_key = 'ThisIsSecret'
@app.route('/')
def login():
if 'red' in session:
	 pass
else:
	session['red'] = 0
if 'green' in session:
	 pass
else:
	session['green'] = 0
if 'blue' in session:
	 pass
else:
	session['blue'] = 0

	return render_template('index.html', red = session['red'], green =session['green'], blue = session=['blue'])

@app.route('/process', methods =['POST'])
def process():
	session['red'] = request.form['red']
	session['green']= request.form['green']
	session['blue'] = request.form['blue']
	

	return redirect('/')



app.run(debug=True) 