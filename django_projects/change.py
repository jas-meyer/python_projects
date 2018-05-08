def change(cent):
	coins = {}
	coins['dollars'] = cent / 100
	cent = cent % 100
	coins['quarters'] = cent /25
	cent = cent % 25
	coins['dimes'] = cent / 10
	cent = cent % 10
	coins['nickels'] = cent / 5
	cent = cent % 5
	coins['pennies'] = cent
	return coins


print change(415)
	
