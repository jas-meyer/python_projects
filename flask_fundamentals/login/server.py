from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
import os, binascii

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX  = re.compile(r'^[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'YourMomsHouse'
mysql = MySQLConnector(app,'login')
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
        if 'email' in session:
            session['email']= request.form['email']
        else: 
            session['email'] = ""
        
    if len(request.form['firstname']) < 2:
        flash("First Name is Invalid!")
        return redirect('/')
    elif not NAME_REGEX.match(request.form['firstname']):
        flash("Invalid Name!")
        return redirect('/')
    if len(request.form['lastname']) < 2:
        flash("Last Name is Invalid!")
        return redirect('/')
    elif not NAME_REGEX.match(request.form['lastname']):
        flash("Invalid Name!")
        return redirect('/')
    
        
    if request.form['password'] != request.form['confirm']:
        flash("The confirmation Password must match the password")
        return redirect('/') 
    else:
        if len(request.form['password']) < 1:
            flash("Password cannot be blank!")
            return redirect('/')
        elif len(request.form['password']) < 8:
            flash("The password needs to be at least 8 characters!")
            return redirect('/')
       
            
        if len(request.form['confirm']) < 1:
            flash("Confirm Password cannot be blank!")
            return redirect('/')
        elif (request.form['confirm'] < 8):
            flash("The password needs to be at least 8 characters!")
            return redirect('/')
        else:
            password = request.form['password']
            salt = binascii.b2a_hex(os.urandom(15))
            hashed_password = md5.new(password + salt).hexdigest()
            query = "INSERT INTO login (email, password, first_name, last_name, salt, created_at, updated_at) VALUES (:email,:password,:first_name, :last_name, :salt,NOW(), NOW())"
            data ={
                    'email': request.form['email'],
                    'first_name': request.form['firstname'],
                    'last_name': request.form['lastname'],
                    'password': hashed_password,
                    'salt' : salt
                    }
            mysql.query_db(query, data)
        
    # login 
    return redirect('/success')
@app.route('/login')
def login():
    

    return render_template("login.html")


@app.route('/process2', methods=['POST'])
def logging():
    email = request.form['logemail']
    if (len(request.form['logemail']) < 1)  and (len(request.form['logpassword'])< 1):            
        print "You need to fill out both passes"
    else:
        user_query = "SELECT * FROM login WHERE email = :email LIMIT 1"
        query_data = {'email': email}
        user = mysql.query_db(user_query, query_data)
        if len(user) != 0:
            encrypted_password = md5.new(request.form['logpassword'] + user[0]['salt']).hexdigest()
            if user[0]['password'] == encrypted_password:
                print "success"
            else:
                print "boo"
     
    return redirect('/success')
@app.route('/success')
def good():
    


    #print session['email']

    return render_template("success.html") #allemail= email)

app.run(debug=True)