from flask import Flask, render_template, request, redirect  # Import Flask to allow us to create our app.
app = Flask(__name__)   

@app.route('/')
def login():
	return render_template('index.html')

@app.route('/process', methods =['POST'])
def process():
	name = request.form['name']
	print "Name:",name
	return redirect('/')


app.run(debug=True) 