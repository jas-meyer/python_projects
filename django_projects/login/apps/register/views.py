from django.shortcuts import render, redirect
import bcrypt
from models import User
from django.contrib import messages
def index(request):

	return render(request,"register/index.html")
def create(request):
	email = str(request.POST['email'])
	a = User.objects.filter(email = email)
	errors = User.objects.basic_validator(request.POST , a)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags = tag)
			print messages.error
		return redirect('/')
	password = str(request.POST['password'])
	hash1 = bcrypt.hashpw(password .encode(), bcrypt.gensalt())
	firstname = str(request.POST['firstname'])
	lastname = str(request.POST['lastname'])
	email = str(request.POST['email'])
	User.objects.create(first_name = firstname, last_name = lastname, email = email, password = hash1) 
	request.session['firstname'] = firstname
	return redirect('/success')
def login(request):
	email = str(request.POST['logemail'])
	a = User.objects.filter(email = email)
	errors = User.objects.password_check(request.POST, a)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags = tag)
			print errors
		return redirect('/')
	
	else:
		request.session['firstname']=a[0].first_name
		print request.session['firstname']
		return redirect('/success')
		
def success(request):

	return render(request,"register/success.html")

# Create your views here.
