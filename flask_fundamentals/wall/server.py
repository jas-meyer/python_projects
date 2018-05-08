from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
import os, binascii

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX  = re.compile(r'^[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'YourMomsHouse'
mysql = MySQLConnector(app,'wall')
@app.route('/')
def index():
    

    return render_template('login.html')
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
            query = "INSERT INTO users ( first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name,:last_name,:email,:password,:salt,NOW(), NOW())"
            data ={
                    'email': request.form['email'],
                    'first_name': request.form['firstname'],
                    'last_name': request.form['lastname'],
                    'password': hashed_password,
                    'salt' : salt
                    }
            mysql.query_db(query, data)
        
    # login 
    return redirect('/wall')
@app.route('/register')
def register():
    

    return render_template("register.html")


@app.route('/process2', methods=['POST'])
def logging():
    email = request.form['logemail']
    if (len(request.form['logemail']) < 1)  and (len(request.form['logpassword'])< 1):            
        print "You need to fill out both passes"
    else:
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        query_data = {'email': email}
        user = mysql.query_db(user_query, query_data)
        if len(user) != 0:
            encrypted_password = md5.new(request.form['logpassword'] + user[0]['salt']).hexdigest()
            if user[0]['password'] == encrypted_password:
                print "success"
                if 'id' in session:
                    session['id']= user[0]['id']
                else: 
                    session['id'] = " " 
                return redirect('/wall')
            else:
                print "boo"
        
    return redirect('/')
@app.route('/wall')
def good():
    if session['id'] == " ":
        return redirect('/')
    else:
    #user_id = session['id']
    #user_query = "SELECT * FROM messages WHERE user_id = :user_id"
        user_query = "SELECT CONCAT(first_name, ' ',last_name) AS name, users.id, messages.id AS messy, message, messages.created_at FROM users JOIN messages ON users.id = user_id"
    #query_data = {'user_id': user_id}
        messages = mysql.query_db(user_query)
        user_query = "SELECT comments.comment as comm, comments.message_id as messy2, comments.created_at as commentcreate, CONCAT(first_name, ' ',last_name) AS name  FROM comments JOIN users on users.id = comments.user_id"
        comments = mysql.query_db(user_query)
    
 

    #print session['email']

    return render_template("wall.html", allmessage = messages, allcomment = comments ) #allemail= email)
@app.route('/message', methods=['POST'])
def message():
    if len(request.form['message']) < 1:
        print "message is blank"
        return redirect('/wall')
    else:
        query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:id,:message, NOW(), NOW())"
        data ={
                    'id': session['id'],
                    'message': request.form['message'],

                    
                    }
        mysql.query_db(query, data)
    return redirect('/wall')   
@app.route('/comment/<messy>', methods=['POST'])
def comment(messy):
    
    print request.form['comment'] 
    if len(request.form['comment']) < 1:
        print "comment is blank"
    else:
        
        query = "INSERT INTO comments (user_id, comment, message_id, created_at, updated_at) VALUES (:id,:comment,:messageid,NOW(), NOW())"
        data ={
                    'id': session['id'],
                    'comment': request.form['comment'],
                    'messageid': int(messy)
            }
        mysql.query_db(query, data)
    return redirect('/wall')
@app.route('/logout')
def logout():
    session['id'] = " "

    return redirect('/')      
app.run(debug=True)