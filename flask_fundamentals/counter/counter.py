from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app.
app = Flask(__name__)   
app.secret_key = 'ThisIsSecret'
@app.route('/')

def login():
	print session
	if "count" in session:
		session['count'] += 1
	else:
		session['count'] = 0

	return render_template('index.html')

"""@app.route('/process', methods =['POST'])
def process():

	session['count'] += 0
	
	return redirect('/')"""

	
	
	

app.run(debug=True) 