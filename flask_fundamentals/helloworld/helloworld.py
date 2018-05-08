from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)   

@app.route('/')
def login():
	return render_template('index.html')

app.run(debug=True) 