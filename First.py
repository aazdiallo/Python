print ("Paycheck computation!\n");
Hours = raw_input("Enter Hours: ");
Rate = raw_input("Enter Rate: ");
try:
	Hours = int(Hours);
	Rate = int(Rate);
	if Hours > 40:
		Pay = 1.5 * Hours * Rate
		print 'Your paycheck for', Hours, 'hours, is:$', round (float(Pay), 2)
	else:
		Pay = Hours * Rate
		print 'Your paycheck for', Hours, 'hours, is:$', round (float(Pay), 2)
except:
	print 'Please enter enteger values \n'
#print Hours*Rate;
