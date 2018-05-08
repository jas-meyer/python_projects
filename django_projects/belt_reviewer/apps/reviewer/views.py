from django.shortcuts import render, redirect
import bcrypt
from models import *
from django.contrib import messages
def index(request):

	return render(request,"reviewer/index.html")
def create(request):
	email = str(request.POST['email'])
	a = User.objects.filter(email = email)
	errors = User.objects.basic_validator(request.POST , a)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags = tag)
			print messages.error
		return redirect('/')
	password = request.POST['password']
	hash1 = bcrypt.hashpw(password .encode(), bcrypt.gensalt())
	name = request.POST['name']
	alias = request.POST['alias']
	email = request.POST['email']
	User.objects.create(name = name, alias = alias, email = email, password = hash1) 
	a = User.objects.filter(email = email)
	request.session['id'] = a[0].id
	request.session['alias'] = a[0].alias
	return redirect('/books')
def login(request):
	email = request.POST['logemail']
	a = User.objects.filter(email = email)
	errors = User.objects.password_check(request.POST, a)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags = tag)
			print errors
		return redirect('/')
	
	else:
		request.session['id'] = a[0].id
		request.session['alias'] = a[0].alias
		return redirect('/books')
		
def success(request):
	a = Review.objects.order_by("-created_at")
	review = []
	exclude = []
	for count in range(3):
		review.append(a[count])
	for c in review:
		this_review = c
		d = c.book
		e = Book.objects.filter(id = d.id)
		f = e[0].id
		exclude.append(f)
		print exclude
	
	context = {
		'books': Book.objects.all(),
		'books2': Book.objects.all().exclude(id =exclude[0]).exclude(id =exclude[1]).exclude(id = exclude[2]), 
		#'reviews': Review.objects.order_by("-created_at"),
		'reviews': review,
		'users': User.objects.all(),
	}

	return render(request,"reviewer/success.html", context)
def add(request):

	return render(request,"reviewer/add.html", {'authors': Author.objects.all()})
def process3(request):
	Author.objects.create(name = request.POST['author'])
	this_author = Author.objects.last()
	a = this_author.id
	print a
	Book.objects.create(title = request.POST['title'], author_id =a)
	this_book = Book.objects.last()
	b = this_book.id
	this_user = User.objects.get(id = request.session['id'])
	this_book.users.add(this_user)
	Review.objects.create(rating = request.POST['rating'], text = request.POST['review'], book_id = b, user_id = request.session['id'])


	return redirect('/books')
def process4(request, id):
	Review.objects.create(rating = request.POST['rating'], text = request.POST['text'], book_id = id, user_id = request.session['id'])
	this_book = Book.objects.get(id = id)
	this_user = User.objects.get(id = request.session['id'])
	this_book.users.add(this_user)
	return redirect('/books')
def delete(request, id):
	b = Review.objects.get(id = id)
	b.delete()
	return redirect('/books')
def book(request, id):

	context = {
		'reviews': Review.objects.all(),
		'users': User.objects.all(),
		'authors': Author.objects.all(),
		'book': Book.objects.get(id = id)
	}
	return render(request,"reviewer/book.html", context)
def user(request, id):
	reviews = Review.objects.all()
	count = 0 
	intid = int(id)
	review = []
	for review in reviews:
		if intid == review.user_id:
			count +=1
	b = Book.objects.filter(users = id)


	context = {
		'user' : User.objects.get(id = id),
		'books' : Book.objects.all(),
		'count' : count,
		'users' : b
	}

	return render(request,"reviewer/user.html", context)
def logout(request):
	del request.session['id']
	del request.session['alias']
	return redirect("/")
# Create your views here.
