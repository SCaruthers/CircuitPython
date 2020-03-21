import time

def deltaPercent(a,b,abs_flag=False):
	# calculate the difference (in percent) between 2 numbers
	if (a==0): return float('Inf')
	result = (b - a)/a
	if abs_flag:
		return abs(result)
	else:
		return result

PURE_WHITE = True
def rgbw(rgb,whiteFlag=not(PURE_WHITE)):
	# change rgb into rgbw with the option to force "white only"
	DeltaThreshold = 0.12 	#the threshold for forcing pure white
	r,g,b = (rgb[0],rgb[1],rgb[2])
	if whiteFlag:
		return (0,0,0,int((r+b+g)/3))
		
	d1 = deltaPercent(r,g,True)
	d2 = deltaPercent(r,b,True)
	d3 = deltaPercent(g,b,True)
	
	if (d1<DeltaThreshold) & (d2<DeltaThreshold) & (d3<DeltaThreshold):
		return (0,0,0,int((r+b+g)/3))
	else:
		return (r,g,b,0)

def color_fade(pixels, color1, color2, wait, steps=20):
    # fade from color1 to color2 in steps and take wait*steps seconds to do it.
    # NOTE: because it takes a finite time to write each pixel (esp. if Brightness <> 1),
    #  the todal duration is much longer than (wait*steps)!
    #
    # This could be re-written to intelligently handle RGB vs RGBW
    r = color1[0]
    g = color1[1]
    b = color1[2]
    w = color1[3]
    d_r = int((color2[0] - color1[0])/steps)
    d_g = int((color2[1] - color1[1])/steps)
    d_b = int((color2[2] - color1[2])/steps)
    d_w = int((color2[3] - color1[3])/steps)
    pixels.fill(color1)
    pixels.show()
    for i in range(0,steps):
        r += d_r
        g += d_g
        b += d_b
        w += d_w
        pixels.fill((r,g,b,w))  #ASSUMING RGBW!!
        pixels.show()
        time.sleep(wait)
    pixels.fill(color2)	#in case of rounding errors, force to end on color2
    pixels.show()