from django.shortcuts import render, redirect
import bcrypt
from models import Course
from django.contrib import messages
def index(request):
	return render(request,"course/index.html", {"courses": Course.objects.all()} )
def process(request):
	errors = Course.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags = tag)
		return redirect('/')
	Course.objects.create(name = request.POST['name'], description = request.POST['des'])
	return redirect('/')
def destroy(request, id):

	return render(request,'course/destroy.html', {"course": Course.objects.get(id = id)})
def delete(request, id):
	b = Course.objects.get(id = id)
	b.delete()
	return redirect('/')

# Create your views here.
