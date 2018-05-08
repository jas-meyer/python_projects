from flask import Flask, render_template, request, redirect, session
import random  # Import Flask to allow us to create our app.
app = Flask(__name__)   
app.secret_key = 'ThisIsSecret'
@app.route('/')

def login():
	if "winnum" in session:
		pass
	else:
		session['winnum'] = random.randrange(0,101)
	if "guess" in session:
		pass
	else:
		session['guess'] = 0
	if "statement" in session:
		pass
	else:
		session['statement'] = ""
	winnum = int(session['winnum'])
	guess = int(session['guess'])
	print session['winnum']
	print session['guess']
	statement = session['statement']
	if guess == 0:
		statement = ""
	elif winnum > guess:
		print "Too Low"
		statement = "Too Low"

	elif winnum < guess:
		print "Too High"
		statement = "Too High"
	elif winnum == guess:
		print "Right On"
		statement = "Right On"
	
	return render_template('index.html', state = statement)

@app.route('/process', methods =['POST'])
def process():
	
	if request.form['guess'] == '':
		print "Enter integer dummy!"
	elif:
		session["guess"]=request.form['guess']
	
	print session["guess"]
	return redirect('/')
@app.route('/reset', methods =['POST'])
def reset():

	session['winnum'] = random.randrange(0,101)
	session['statement'] = ""

	
	return redirect('/')

app.run(debug=True) 