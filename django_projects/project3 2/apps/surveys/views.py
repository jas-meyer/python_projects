from django.shortcuts import render,HttpResponse, redirect
def index(request):

	return render(request, 'surveys/index.html')
def process(request):
	if request.method == "POST":
		if 'counter' in request.session:
			request.session['counter'] += 1
		else: 
			request.session['counter'] = 1
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
	return redirect('/result')
def back(request):

	return redirect('/')
def result(request):

	return render(request, 'surveys/result.html')
# Create your views here.	'/index'
