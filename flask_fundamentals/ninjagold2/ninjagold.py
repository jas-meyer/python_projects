from flask import Flask, render_template, request, redirect, session
import random  # Import Flask to allow us to create our app.
app = Flask(__name__)   
app.secret_key = 'ThisIsSecret'
@app.route('/')

def login():
	if "result" in session:
		pass
	else:
		session['result'] = 0
	if 'total' in session:
		session['total'] += session['result'] 
	else:
		session['total'] = 0
	if "building" in session:
		pass
	else:
		session['building'] = ""
	if "statement" in session:
		pass
	else:
		session['statement'] = ""
	if "statementlist" in session:
		pass
	else:
		session['statementlist'] = []
	if "count" in session:
		session['count'] += 1
	else:
		session['count'] = 0

	count = session['count']
	statementlist = session['statementlist']
	print count
	statement = session['statement']
	result = int(session['result'])
	abresult = abs(result)
	strresult = str(abresult)
	if result > -1:
		print "Earned "+strresult+" golds from the "+session['building']+"!"
		statement = "Earned "+strresult+" golds from the "+session['building']+"!"
		color = 1
		combine = []
		combine.append(statement)
		combine.append(color)
		statementlist.append(combine)
	else:
		print "Entered a casino and lost "+strresult+" golds...Ouch.." 
		statement = "Entered a casino and lost "+strresult+" golds...Ouch.."
		color = 0
		combine = []
		combine.append(statement)
		combine.append(color)
		statementlist.append(combine)
	
	return render_template('index.html', result = result, total = session['total'], statementlist = statementlist, count = session['count'])

@app.route('/process', methods =['POST'])
def process():
	if "result" in session:
		pass
	else:
		session['result'] = 0
	if "building" in session:
		pass
	else:
		session['building'] = ""

	if request.form["building"] == "farm":
		session['result'] = random.randrange(10,21)
		session['building'] = "farm"
		print 1
	elif request.form["building"] == "cave":
		session['result'] = random.randrange(5,11)
		session['building'] = "cave"
		print 2
	elif request.form["building"] == "house":
		session['result'] = random.randrange(2,6)
		session['building'] = "house"
		print 3
	elif request.form["building"] == "casino":
		session['result'] = random.randrange(-50,51)
		session['building'] = "casino"
		print 4


	return redirect('/')
"""@app.route('/reset', methods =['POST'])
def reset():

	session['winnum'] = random.randrange(0,101)
	session['statement'] = ""

	
	return redirect('/')"""

app.run(debug=True) 