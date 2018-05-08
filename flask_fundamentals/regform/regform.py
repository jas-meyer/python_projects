from flask import Flask, render_template, request, redirect, session, flash  # Import Flask to allow us to create our app.
app = Flask(__name__)
import re   
app.secret_key = 'ThisIsSecret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX	= re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[A-Z])')

@app.route('/')
def login():
	return render_template('index.html')

@app.route('/process', methods =['POST'])
def process():
	
	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
	else:
		flash("Success!")
	if len(request.form['firstname']) < 1:
		flash("First Name cannot be blank!")
	elif not NAME_REGEX.match(request.form['firstname']):
		flash("Invalid Name!")
	else:
		flash("Success!")
	if len(request.form['lastname']) < 1:
		flash("Last Name cannot be blank!")
	elif not NAME_REGEX.match(request.form['lastname']):
		flash("Invalid Name!")
	else:
		flash("Success!")
	if request.form['password'] != request.form['confirm']:
		flash("The confirmation Password must match the password") 
	else:
		if len(request.form['password']) < 1:
			flash("Password cannot be blank!")
		elif len(request.form['password']) < 8:
			flash("The password needs to be at least 8 characters!")
		elif not PASSWORD_REGEX.match(request.form['password']):
			flash("You need a password that has a least one Upper Case Letter and one Number!")
		else:
			flash("Success!")
		if len(request.form['confirm']) < 1:
			flash("Confirm Password cannot be blank!")
		elif (request.form['confirm'] < 9):
			flash("The password needs to be at least 8 characters!")
		else:
			flash("Success!")


	print request.form['email']
	print request.form['firstname']
	print request.form['lastname']
	print request.form['password']
	print request.form['confirm']

	return redirect('/')



app.run(debug=True) 