from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
	
    query = 'SELECT CONCAT(first_name," ",last_name) as name, age, CONCAT(MONTHNAME(friend_since)," ",DAYOFMONTH(friend_since)) as monthday, YEAR(friend_since) as year FROM friends'
    friends = mysql.query_db(query)
    print friends

    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, age, friend_since) VALUES (:first_name, :last_name, :age, NOW())"
    name = request.form['name']
    strname = str(name)
    first = strname.split()[0]
    last = strname.split()[1]
    print first
    print last

 
    
    data ={
    		 'first_name': first,
             'last_name': last,
             'age': request.form['age']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)