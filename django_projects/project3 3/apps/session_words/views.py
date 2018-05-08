from django.shortcuts import render,HttpResponse, redirect
from time import gmtime, strftime
import datetime
def index(request):
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 0
	return render(request, 'session_words/index.html')
def add(request):
	word = ""
	big = 0

	if 'words' in request.session:
		
	
		pass

	else:
		request.session['words'] = []
		
	
	
	
	big = int(request.POST['bold'])
	color =str(request.POST['color'])
	words = request.session['words']
	if color == "red":
		col = 0
	elif color == "green":
		col = 1
	else:
		col = 2 
	
	combine = {}
	combine['word'] = request.POST['word'] 
	combine['color'] = col
	combine['big'] = big
	dt = str(datetime.datetime.now().strftime("%I:%M %p %m/%d/%Y").replace('AM', 'am').replace('PM', 'pm'))
	combine['date']= dt
	words.append(combine)
	request.session['words'] = words
	
	
	
	return redirect('/session_words')

def clear(request):
	del request.session['words'] 
	
	return redirect('/session_words')


# Create your views here.
