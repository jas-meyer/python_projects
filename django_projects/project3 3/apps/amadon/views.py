from django.shortcuts import render,HttpResponse, redirect

def index(request):
	
	return render(request, 'amadon/index.html')
def buy(request):
	if 'totquan' in request.session:
		pass
	else: 
		request.session['totquan'] = 0
	if 'total' in request.session:
		pass
	else:
		request.session['total'] = 0
	if 'subtotal' in request.session:
		request.session['subtotal'] = 0
	else: 
		request.session['subtotal'] = 0


	prod_id= int(request.POST['product_id'])
	quan = int(request.POST['quantity'])

	if prod_id== 1001:
		subtotal =  quan * 19.99
		request.session['subtotal'] = subtotal
		request.session['totquan'] += quan
		request.session['total'] += subtotal
	elif prod_id == 1002:
		subtotal = quan * 29.99
		request.session['subtotal'] = subtotal
		request.session['totquan'] += quan
		request.session['total'] += subtotal
	elif prod_id == 1003:
		subtotal = quan * 4.99
		request.session['subtotal'] = subtotal
		request.session['totquan'] += quan
		request.session['total'] += subtotal
	elif prod_id == 1004:
		subtotal = quan * 49.99
		request.session['subtotal'] = subtotal
		request.session['totquan'] += quan
		request.session['total'] += subtotal





	return redirect('/amadon/checkout')
def checkout(request):

	return render(request, 'amadon/checkout.html')