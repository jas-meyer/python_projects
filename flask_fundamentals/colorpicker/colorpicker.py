from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app.
app = Flask(__name__)   
app.secret_key = 'ThisIsSecret'
@app.route('/')
def login():
	if 'red' in session:
		pass
	else:
		session['red'] = 255
	if 'green' in session:
	 	pass
	else:
		session['green'] = 255
	if 'blue' in session:
		pass
	else:
		session['blue'] = 255

	return render_template('index.html', red = session['red'], green = session['green'], blue = session['blue'])

@app.route('/process', methods =['POST'])
def process():
	print request.form['red']
	print request.form['green']
	print request.form['blue']
	if request.form['red'] == None:
		session['red'] = 0
		print session['red']
	#elif request.form['red'] > 255:
	#	session['red'] = 255
	else:
		session['red'] = request.form['red']
	if request.form['green'] == None:
		session['greed'] = 0
	#elif request.form['green'] > 255:
	#	session['green'] = 255
	else:
		session['green']= request.form['green']
	if request.form['blue'] == None:
		session['blue'] = 0
	#elif request.form['blue'] > 255:
	#	session['blue'] = 255
	else:
		session['blue'] = request.form['blue']
	

	return redirect('/')



app.run(debug=True) 