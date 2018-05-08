from flask import Flask, render_template, request, redirect  # Import Flask to allow us to create our app.
app = Flask(__name__)   

@app.route('/')
def login():
	return render_template('index.html')

@app.route('/ninja')
def ninja():
	
	return render_template('ninjas.html')
@app.route('/ninja/blue')
def blue():
	
	return render_template('blue.html')
@app.route('/ninja/orange')
def orange():
	
	return render_template('orange.html')
@app.route('/ninja/red')
def red():
	
	return render_template('red.html')
@app.route('/ninja/purple')
def purple():
	
	return render_template('purple.html')
@app.route('/ninja/<variable>')
def april(variable):
	
	return render_template('notapril.html')



app.run(debug=True) 