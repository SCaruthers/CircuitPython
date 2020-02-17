def deltaPercent(a,b,abs_flag=False):
	# calculate the difference (in percent) between 2 numbers
	result = (b - a)/a
	if abs_flag:
		return abs(result)
	else:
		return result

PURE_WHITE = True
def rgbw(r,g,b,whiteFlag=not(PURE_WHITE)):
	# chang rgb into rgbw with the option to force "white only"
	DeltaThreshold = 0.10 	#the threshold for forcing pure white
	
	if whiteFlag:
		return (0,0,0,int((r+b+g)/3))
		
	d1 = deltaPercent(r,g,True)
	d2 = deltaPercent(r,b,True)
	d3 = deltaPercent(g,b,True)
	
	if (d1<DeltaThreshold) & (d2<DeltaThreshold) & (d3<DeltaThreshold):
		return (0,0,0,int((r+b+g)/3))
	else:
		return (r,g,b,0)
	

