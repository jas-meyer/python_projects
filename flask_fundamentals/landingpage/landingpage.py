from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)   

@app.route('/')
def login():
	return render_template('index.html')

@app.route('/ninjas')
def project():
	return render_template('ninjas.html')

@app.route('/dojos/new')
def about():
	return render_template('dojos.html')

app.run(debug=True) 