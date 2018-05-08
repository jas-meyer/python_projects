from django.shortcuts import render,HttpResponse, redirect
import datetime, random
from time import gmtime, strftime

def index(request):

	return render(request, 'ninjagold/index2.html')
def process(request):
	if "result" in request.session:
		pass
	else:
		request.session['result'] = 0
	if 'total' in request.session:
		pass
	else:
		request.session['total'] = 0
	
	if "building" in request.session:
		pass
	else:
		request.session['building'] = ""
	if "statement" in request.session:
		pass
	else:
		request.session['statement'] = ""
	if "statementlist" in request.session:
		pass
	else:
		request.session['statementlist'] = []
	if "count" in request.session:
		pass
	else:
		request.session['count'] = 0



	if request.POST["building"] == "farm":
		request.session['result'] = random.randrange(10,21)
		request.session['building'] = "farm"
		print 1
	elif request.POST["building"] == "cave":
		request.session['result'] = random.randrange(5,11)
		request.session['building'] = "cave"
		print 2
	elif request.POST["building"] == "house":
		request.session['result'] = random.randrange(2,6)
		request.session['building'] = "house"
		print 3
	elif request.POST["building"] == "casino":
		request.session['result'] = random.randrange(-50,51)
		request.session['building'] = "casino"
		print 4
	dt = str(datetime.datetime.now().strftime("%I:%M %p %d/%m/%Y").replace('AM', 'am').replace('PM', 'pm'))
	count = request.session['count']
	print request.session['statementlist']
	statementlist = request.session['statementlist']
	print count
	result = request.session['result']
	statement = request.session['statement']
	request.session['total'] += request.session['result']
	
	request.session['count'] += 1
	result = int(request.session['result'])
	abresult = abs(result)
	strresult = str(abresult)
	if result > -1:
		print "Earned "+strresult+" golds from the "+request.session['building']+"!"
		statement = "Earned "+strresult+" golds from the "+request.session['building']+"! "+"("+dt+")"
		color = 1
		combine = {}
		combine['statement']=statement 
		combine['color'] = color
		statementlist.append(combine)
	else:
		print "Entered a casino and lost "+strresult+" golds...Ouch.."
		statement = "Entered a casino and lost "+strresult+" golds...Ouch.. "+"("+dt+")"
		color = 0
		combine = {}
		combine['statement']=statement 
		combine['color'] = color
		statementlist.append(combine)

	#request.session['result'] = None
	print statementlist

	return redirect('/ninjagold')
def clear(request):
	del request.session['total']
	del request.session['statementlist']
	return redirect('/ninjagold')
# Create your views here.
