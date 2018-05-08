from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'YourMomsHouse'
mysql = MySQLConnector(app,'email_vaild')
@app.route('/')
def index():
    

    return render_template('index.html')
@app.route('/process', methods=['POST'])
def create():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        query = "INSERT INTO email (email,created_at,updated_at) VALUES (:email, NOW(), NOW())"
        data ={
    		 'email': request.form['email']
             
           }
        if 'email' in session:
            session['email']= request.form['email']
        else: 
            session['email'] = ""
    # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
    return redirect('/success')
@app.route('/success')
def good():
    query = "SELECT email, DATE_FORMAT(created_at,'%m/%d/%Y  %I:%i%p')as datetime FROM email"
    email = mysql.query_db(query)

    print session['email']

    return render_template("success.html", allemail= email)

app.run(debug=True)