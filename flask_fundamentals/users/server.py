from flask import Flask, request, redirect, render_template, session, flash, url_for
from mysqlconnection import MySQLConnector
import re
import md5
import os, binascii

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX  = re.compile(r'^[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'YourMomsHouse'
mysql = MySQLConnector(app,'users')
@app.route('/users')
def index():
    user_query = "SELECT user.id,CONCAT(first_name, ' ',last_name)as name, email, DATE_FORMAT(created_at, '%M %D, %Y')as created FROM USER"
    user = mysql.query_db(user_query)

    return render_template('index.html', alluser = user)
@app.route('/users/create', methods=['POST'])
def create():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/users')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/users/new')
    else:
        if 'email' in session:
            session['email']= request.form['email']
        else: 
            session['email'] = ""
        
    if len(request.form['firstname']) < 2:
        flash("First Name is Invalid!")
        return redirect('/users/new')
    elif not NAME_REGEX.match(request.form['firstname']):
        flash("Invalid Name!")
        return redirect('/users')
    if len(request.form['lastname']) < 2:
        flash("Last Name is Invalid!")
        return redirect('/users/new')
    elif not NAME_REGEX.match(request.form['lastname']):
        flash("Invalid Name!")
        return redirect('/users/new')
    else:
        
            query = "INSERT INTO user ( first_name, last_name, email, created_at, updated_at) VALUES (:first_name,:last_name,:email,NOW(), NOW())"
            data ={
                    'email': request.form['email'],
                    'first_name': request.form['firstname'],
                    'last_name': request.form['lastname'],
                    
                    }
            mysql.query_db(query, data)
            user_query = "SELECT user.id,first_name, last_name, email, DATE_FORMAT(created_at, '%M %D, %Y')as created FROM user WHERE email = :email LIMIT 1"
            query_data = {'email': request.form['email'] }
            user = mysql.query_db(user_query, query_data)

    # login 
    return redirect(url_for('show', id =  user[0]['id']))
@app.route('/users/new')
def new():
        

    return render_template('new.html')
@app.route('/users/<id>', methods=['POST']) 
def update(id):
    print request.form['firstname']
    query = "UPDATE user SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
    data = {
             'first_name': request.form['firstname'],
             'last_name':  request.form['lastname'],
             'email': request.form['email'],
             'id' : id
             
           }
   
    mysql.query_db(query, data)
    print id
    print type(id)
    intid = int(id)
    return redirect(url_for('show', id = id))
@app.route('/users/<id>') 
def show(id):
    user_query = "SELECT user.id,CONCAT(first_name, ' ',last_name)as name, email, DATE_FORMAT(created_at, '%M %D, %Y')as created FROM user WHERE id = :id LIMIT 1"
    query_data = {'id': id }
    user = mysql.query_db(user_query, query_data)
    

    return render_template('show.html', user =user)

@app.route('/users/<id>/edit')
def edit(id):
    user_query = "SELECT user.id,first_name, last_name, email, DATE_FORMAT(created_at, '%M %D, %Y')as created FROM user WHERE id = :id LIMIT 1"
    query_data = {'id': id }
    user = mysql.query_db(user_query, query_data)
    return render_template('edit.html', user =user)
@app.route('/users/<id>/destroy') 
def destroy(id):
    
    query = "DELETE FROM user WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)

    return redirect('/users')



"""@app.route('/register')
def register():
    

    return render_template("register.html")


@app.route('/process2', methods=['POST'])
def logging():' object has no attribute 'id'
127.0.0.1 - - [18/Feb/2018 13:11:54] "GET /users/3?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 200 -
127.0.0.1 - - [18/Feb/2018 13:11:54] "GET /users/3?__debugger__=yes&cmd=resource&f=jquery.js HTTP/1.1" 200 -
127.0.0.1 - - [18/Feb/2018 13:11:54] "GET /users/3?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 200 -
127.0.0.1 - - [18/Feb/2018 13:11:54] "GET /users/3?__debugger__=yes&cmd=resource&f=ubuntu.ttf HTTP/1.1" 200 -
127.0.0.1 - - [18/Feb/2018 13:11:54] "GET /users/3?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 200 -
127.0.0.1 - - [18/Feb/2018 13:11:54] "GET /users/3?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 200 -
 * Detected change in '/Users/jasonmeyer/Desktop/pythonstack/flask_fundamentals/users/server.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 215-960-371
 * Detected change in '/Users/jasonmeyer/Desktop/pythonstack/flask_fundamentals/users/server.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 215-960-371
 * Detected change in '/Users/jasonmeyer/Desktop/pythonstack/flask_fundamentals/users/server.py', reloading
 * Restarting with stat
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

    return redirect('/')"""      
app.run(debug=True)