import math

class ColorRGB():
	'''
		This class is using for color info containing
		Also it make string in hex format
		Example:
		If you want to use color which red = 100, green = 15, blue = 45
		it will contain that data and give you a string "#640f2d"
		(This string is necesary for TKinter drawing)
	'''
	def __init__(self, red, green, blue):
		flag = True
		while flag:
			#print("red" ,red)
			#print("green",green)
			#print("blue",blue)
			if (red <= 255 and red >= 0 and green <= 255 and green >=0 and blue >= 0 and blue <=255 ) :
				flag = False
				self.red = red			
				self.green = green
				self.blue = blue
				self.inHex = self.toHex()
				self.toAHSL()
			elif (red > 255):
				red = red - 256
			elif (red < 0 ):
				red = red + 256
			elif (blue > 255):
				blue = blue - 256
			elif (blue < 0 ):
				blue = blue + 256		
			elif (green > 255):
				green = green - 256
			elif (green < 0 ):
				green = green + 256	
				

	# This method uses type ColorRGB (i defined it)
	def toHex (self):
		red = self.red
		green = self.green
		blue = self.blue
		answer = "#"
		while True:
			if (red <= 255 and red >= 0 and green <= 255 and green >=0 and blue >= 0 and blue <=255 ) :
				return "#%02x%02x%02x" % (round(red), round(green), round(blue))
			elif (red > 255):
				red = red - 256
			elif (red < 0 ):
				red = red + 256
			elif (blue > 255):
				blue = blue - 256
			elif (blue < 0 ):
				blue = blue + 256		
			elif (green > 255):
				green = green - 256
			elif (green < 0 ):
				green = green + 256	
			else : 
				return False
				
	def toAHSL(self):
		r = self.red
		g = self.green
		b = self.blue
		max = 0
		min = 256
		
		if (r > max):
			max = r
		if (g > max):
			max = g
		if (b > max):
			max = b
		if (r < min):
			min = r
		if (g < min):
			min = g
		if (b < min):
			min = b
		
		if (max == min):
			h = 0
		elif ((max == r) and (g >= b)):
			h = 60 * (g - b) / (max - min) + 0
		elif ((max == r) and (g <= b)):
			h = 60 * (g - b) / (max - min) + 360
		elif (max == g):
			h = 60 * (b - r) / (max - min) + 120
		elif (max == b):
			h = 60 * (b - g) / (max - min) + 240	
		gray = (r + g + b)/3
		
		r0 = 0
		g0 = 0
		b0 = 0
		
		if (h >= 0 and h <= 60):
			r0 = 255
			g0 = 4.25 * h
		if (h > 60 and h <= 120):
			g0 = 255
			r0 = 255 - 4.25 * (h - 60)
		if (h > 120 and h <= 180):
			g0= 255
			b0 = 4.25 * (h - 120)
		if (h > 180 and h <= 240):
			b0 = 255
			g0 = 255 - 4.25 * (h - 180)
		if (h > 240 and h <= 300):
			b0 = 255
			r0 = 4.25 * (h - 240)
		if (h > 300 and h <= 360):
			r0 = 255
			b0 = 255 - 4.25 * (h - 300)
		
		gray0 = (r0 + g0 + b0)/3
		
		if (gray == gray0):
			l = 0
		if (gray > gray0):
			l = 100*(gray - gray0) / (255 - gray0)
		if (gray < gray0):
			l = 100*(gray - gray0) / gray0
		
		if (l > 0):
			r0 = r0 + l*(255 - r0)/ 100
		if (l < 0):
			r0 += l * r0 / 100
			
		if (r == gray):
			s = 0
		else:
			s = 255 * abs(r - gray) / abs(r0 -gray)
		
		self.hue = round(h)
		self.light = round(l)
		self.sat = round(s)
	
	def getAHSLmodel(self):
		return ColorAHSL(self.hue, self.sat, self.light)
		

class ColorAHSL(ColorRGB):
	
	def __init__(self, hue, sat, light):
		#answer = #
		#rgbForm = toRgb(self)
		flag = True
		while flag:
			if (hue <= 360 and hue >= 0 and sat <= 255 and sat >=0 and light >= -100 and light <=100 ) :
				self.hue = round(hue)
				self.sat = round(sat)
				self.light = round(light)
				flag = False
			elif (hue > 360):
				hue = hue - 360
			elif (hue < 0 ):
				hue = hue + 360
			elif (light > 100):
				light = light - 200
			elif (light < -100 ):
				light = light + 200		
			elif (sat > 255):
				sat = sat - 255
			elif (sat < 0 ):
				sat = sat + 255
			else : 
				flag = False
			
	def toRgb(self):
		h = self.hue
		l = self.light
		s = self.sat
		
		r = 0
		g = 0
		b = 0
		
		if (h >= 0 and h <= 60):
			r = 255
			g = 4.25 * h
		if (h > 60 and h <= 120):
			g = 255
			r = 255 - 4.25 * (h - 60)
		if (h > 120 and h <= 180):
			g= 255
			b = 4.25 * (h - 120)
		if (h > 180 and h <= 240):
			b = 255
			g = 255 - 4.25 * (h - 180)
		if (h > 240 and h <= 300):
			b = 255
			r = 4.25 * (h - 240)
		if (h > 300 and h <= 360):
			r = 255
			b = 255 - 4.25 * (h - 300)
			
		if (l > 0):
			r = r + l*(255 - r)/ 100	
			g = g + l*(255 - g)/ 100
			b = b + l*(255 - b)/ 100
			
		if (l < 0):
			r += l * r / 100	
			g += l * g / 100	
			b += l * b / 100	
			
		gray = (r + g + b)/3
		
		self.red = round(gray + (s * (r - gray))/255)
		self.blue = round(gray + (s * (b - gray))/255)
		self.green = round(gray + (s * (g - gray))/255)
		
	def toHex (self):
		self.toRgb()
		print(round(self.hue))
		print(round(self.sat))
		print(round(self.light))
		print("#%02x%02x%02x" % (round(self.red), round(self.green), round(self.blue)))
		#print(round(self.green))
		#print(round(self.blue))
		
		return "#%02x%02x%02x" % (round(self.red), round(self.green), round(self.blue))

class Coord():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def offset(self, sin, cos, n):
		self.x += cos*n
		self.y += sin*n
		
#class Vertexes(start, sin, cos, n):
#	pass

class Cube():
	def __init__(self, w, start, color):
		self.startX = startX = start.x
		self.startY = startY = start.y
		self.start = Coord(self.startX, self.startY)
		self.stepColor = 5
		self.red = 0
		self.green = 0 
		self.blue = 0 
		self.setSizeOfCube()
		
		self.stepX = stepX = 3
		self.angleK = 0.6 # k < 1 ! 
		self.stepY = stepY = self.stepX * self.angleK
		
		self.sizeX=math.ceil(self.stepX * 2)
		self.sizeY=math.ceil(self.stepX * 2)
		self.start = start
		self.everyObj = []
		
		
		
		self.colorToCoords(w, color)
		self.findPoint()
		self.resetDraw(self.blue, w)
	
	def findPoint(self):
		self.a = a = Coord (self.startX, self.startY )
		self.b = b = Coord (a.x + self.aosY * self.stepX, a.y - self.aosY * self.stepY )
		self.c = c = Coord (b.x + self.aosX * self.stepX, b.y + self.aosX * self.stepY )
		self.d = d = Coord (c.x - self.aosY * self.stepX, c.y + self.aosY * self.stepY )
		self.e = e = Coord (a.x, a.y + self.aosZ * self.stepX )
		self.f = f = Coord (b.x, b.y + self.aosZ * self.stepX )
		self.g = g = Coord (c.x, c.y + self.aosZ * self.stepX )
		self.h = h = Coord (d.x, d.y + self.aosZ * self.stepX )		
		self.m = m = Coord (a.x + self.blue * self.stepX, a.y - self.blue * self.stepY)
		self.n = n = Coord (m.x + self.aosX * self.stepX, m.y + self.aosX * self.stepY)
		self.o = o = Coord (n.x, n.y + self.aosZ * self.stepX)
		self.p = p = Coord (m.x, m.y + self.aosZ * self.stepX)
		self.q = q = Coord (m.x + self.red * self.stepX, m.y + self.red * self.stepY)
		self.r = r = Coord (q.x, q.y + self.aosZ * self.stepX)
		self.s = s = Coord (m.x, m.y + self.green * self.stepX)
		self.t = t = Coord (n.x, n.y + self.green * self.stepX)		
		
		
	def setSizeOfCube(self):
		self.amountOfSteps = round(255/self.stepColor)
		self.aosX = self.amountOfSteps
		self.aosY = self.amountOfSteps
		self.aosZ = self.amountOfSteps
		

	def colorToCoords(self, w, color):
		start = round(color.blue / self.stepColor)
		x = round(color.red / self.stepColor) + self.stepX*start
		y = (self.amountOfSteps * self.stepX) - round(color.green / 5) + self.stepX*start
		self.blue = start
		self.red = round(color.red / self.stepColor)
		self.green = round((256 - color.green)/ self.stepColor)
		#self.resetDraw(start, w) 
		
	def resetDraw(self, start, w):
		#self.deleteAll(w)
		self.start = start;
		self.drawBackEdges(w, ColorRGB(140,140,140).toHex(), self.sizeX*0.75)
		self.drawTop(w)
		self.drawRight(w)
		self.drawFront(w)
		self.drawFrontEdges(w, ColorRGB(40,40,40).toHex(), self.sizeX*0.75)
		self.frontEdge(w, ColorRGB(40,40,40).toHex(), self.sizeX*0.75)	

	def drawTop(self, w):
		pass
	
	def drawRight(self, w):
		pass
	
	def drawFront(self, w):
		pass
	
	def drawEdge (self, w, startPoint, endPoint, color, wid):
		w.create_line(startPoint.x, startPoint.y, endPoint.x, endPoint.y, fill = color, width = wid)
		return w
		
	def drawBackEdges(self, w, color, wid): 
		# back-right and back-left B - F
		self.drawEdge(w, self.b, self.f, color, wid)
		
		# back-left and bottom E - F  
		self.drawEdge(w, self.e, self.f, color, wid)
					    
		# back-right and bottom	G - F	  
		self.drawEdge(w, self.g, self.f, color, wid)	
			
		return w
		
	def drawFrontEdges(self, w, color, wid): 	
		# back-left and top A - B
		self.drawEdge(w, self.a, self.b, color, wid)	
					  
		# back-right and top B - C
		self.drawEdge(w, self.b, self.c, color, wid)		
					  						  
		# front-right and top C - D
		self.drawEdge(w, self.c, self.d, color, wid)	
					  		  
		# front-right and front-left D - H
		self.drawEdge(w, self.d, self.h, color, wid)
					  		
		# front-left and top A - D
		self.drawEdge(w, self.a, self.d, color, wid)
		
		# front-left and bottom	E - H 
		self.drawEdge(w, self.e, self.h, color, wid)
					  					  
		# front-right and bottom H - G			  
		self.drawEdge(w, self.h, self.g, color, wid)
					  
		# front-left and back-left A - E		  
		self.drawEdge(w, self.a, self.e, color, wid)
					  
		# front-right and back-right C - G			  
		self.drawEdge(w, self.c, self.g, color, wid)
		
			
	def frontEdge(self, w, color, wid):
		#top M - N
		self.drawEdge(w, self.m, self.n, color, wid)
		
		#right N - O												
		self.drawEdge(w, self.o, self.n, color, wid)
		
		#bottom P - O
		self.drawEdge(w, self.o, self.p, color, wid)
		
		#left M - P
		self.drawEdge(w, self.m, self.p, color, wid)
		
								
		#vertical Q - R
		self.drawEdge(w, self.q, self.r, color, 1)
		
		#horizontal S - T
		self.drawEdge(w, self.s, self.t, color, 1)
		
		return w	  
			
		
		
class RGBCube(Cube):	
	def __init__(self, w, start, color):     #Init constructor of superclass and some		
		Cube.__init__(self, w, start, color) 
		
			
		
#	def drawCross(self, w, color) 	
       	
	def drawTop(self, w):
		x1 = self.startX
		y1 = self.startY
		col = ColorRGB(0, 255, 0)
		for i in range(0, self.aosX):
			col.blue = 0
			foo = x1
			bar = y1
			x1 = self.stepX + x1
			y1 = self.stepY + y1
			col.red += self.stepColor
			for j in range(0, self.aosY):
				foo = foo + self.stepX
				bar = bar - self.stepY
				col.blue += self.stepColor
				if (j > self.blue) :
					 rec = w.create_rectangle(foo, bar, foo + self.sizeX, bar + self.sizeY, fill=col.toHex(), width=0)
					 self.everyObj.append(rec)
					
	def drawFront(self, w):
		#x1 = self.startX + self.stepX * self.blue
		#y1 = self.startY - self.stepY * self.blue
		x1 = self.m.x
		y1 = self.m.y
		col = ColorRGB(0, 255, 0 + self.blue * self.stepColor)
		for i in range(0, self.aosZ):
			col.red = 0
			foo = x1
			bar = y1
			y1 = y1 + self.stepX
			col.green = col.green - self.stepColor
			for j in range(0, self.aosX - 1):
				foo = foo + self.stepX
				bar = bar + self.stepY
				col.red = col.red + self.stepColor
				rec = w.create_rectangle(foo, bar, foo + self.sizeX, bar + self.sizeY, fill=col.toHex(), width=0)
				self.everyObj.append(rec)
				
	def drawRight(self, w):
		#x1 = self.startX + (self.amountOfSteps - 1) * self.stepX
		#y1 = self.startY + (self.amountOfSteps - 1) * self.stepY
		x1 = self.d.x - self.stepX
		y1 = self.d.y 
		col = ColorRGB(255, 255,0)
		
		for i in range(0, self.aosZ - 1):
			col.blue=0
			foo=x1
			bar=y1
			y1 = y1 + self.stepX
			col.green = col.green - self.stepColor
			for j in range(0, self.aosY - 1):
				foo = foo + self.stepX
				bar = bar - self.stepY
				col.blue = col.blue + self.stepColor
				if (j > self.blue) :
					self.everyObj.append(w.create_rectangle(foo, bar, foo + self.sizeX, bar + self.sizeY, fill=col.toHex(), width=0))
					

	
	def deleteAll(self, w):
		for i in self.everyObj:
			w.delete(i)
			

class AHSLCube(Cube):	
		
	def setSizeOfCube(self):
		self.amountOfSteps = round(255/self.stepColor)
		self.aosX = round(200/self.stepColor)
		self.aosY = round(360/self.stepColor)
		self.aosZ = round(255/self.stepColor)	
		
	def findPoint(self):
		self.a = a = Coord (self.startX, self.startY )
		self.b = b = Coord (a.x + self.aosY * self.stepX, a.y - self.aosY * self.stepY )
		self.c = c = Coord (b.x + self.aosX * self.stepX, b.y + self.aosX * self.stepY )
		self.d = d = Coord (c.x - self.aosY * self.stepX, c.y + self.aosY * self.stepY )
		self.e = e = Coord (a.x, a.y + self.aosZ * self.stepX )
		self.f = f = Coord (b.x, b.y + self.aosZ * self.stepX )
		self.g = g = Coord (c.x, c.y + self.aosZ * self.stepX )
		self.h = h = Coord (d.x, d.y + self.aosZ * self.stepX )		
		self.m = m = Coord (a.x + self.hue * self.stepX, a.y - self.hue * self.stepY)
		self.n = n = Coord (m.x + self.aosX * self.stepX, m.y + self.aosX * self.stepY)
		self.o = o = Coord (n.x, n.y + self.aosZ * self.stepX)
		self.p = p = Coord (m.x, m.y + self.aosZ * self.stepX)
		self.q = q = Coord (m.x + (self.light + 50) * self.stepX, m.y + (self.light + 50) * self.stepY)
		self.r = r = Coord (q.x, q.y + self.aosZ * self.stepX)
		self.s = s = Coord (m.x, m.y + self.sat * self.stepX)
		self.t = t = Coord (n.x, n.y + self.sat * self.stepX)		
		
	def colorToCoords(self, w, color):
		#x = round(color.red / self.stepColor) + self.stepX*start
		#y = (self.amountOfSteps * self.stepX) - round(color.green / self.stepColor) + self.stepX*start
		self.hue = round(color.hue / self.stepColor)
		self.light = round(color.light / self.stepColor)
		self.sat = round((256 - color.sat)/ self.stepColor)	
					
	def drawTop(self, w):
		x1 = self.startX
		y1 = self.startY
		col = ColorAHSL(0, 255, -100)
		for i in range(0, self.aosX):
			col.hue = 0
			foo = x1
			bar = y1
			x1 = self.stepX + x1
			y1 = self.stepY + y1
			col.light += self.stepColor
			for j in range(0, self.aosY):
				foo = foo + self.stepX
				bar = bar - self.stepY
				col.hue += self.stepColor
				#if (j > self.hue) :
				if (j > self.hue) :
					 rec = w.create_rectangle(foo, bar, foo + self.sizeX, bar + self.sizeY, fill=col.toHex(), width=0)
					 self.everyObj.append(rec)
					 
	def drawFront(self, w):
		#x1 = self.startX + self.stepX * self.blue
		#y1 = self.startY - self.stepY * self.blue
		x1 = self.m.x
		y1 = self.m.y
		col = ColorAHSL(0 + self.hue * self.stepColor, 255, -100)
		for i in range(0, self.aosZ):
			col.light = -100
			foo = x1
			bar = y1
			y1 = y1 + self.stepX
			col.sat = col.sat - self.stepColor
			for j in range(0, self.aosX):
				foo = foo + self.stepX
				bar = bar + self.stepY
				col.light = col.light + self.stepColor
				print ("step",j)
				rec = w.create_rectangle(foo, bar, foo + self.sizeX, bar + self.sizeY, fill=col.toHex(), width=0)
				self.everyObj.append(rec)
				
	def drawRight(self, w):
		#x1 = self.startX + (self.amountOfSteps - 1) * self.stepX
		#y1 = self.startY + (self.amountOfSteps - 1) * self.stepY
		x1 = self.d.x - self.stepX
		y1 = self.d.y 
		col = ColorAHSL(0, 255, 100)
		
		for i in range(0, self.aosZ - 1):
			col.hue=0
			foo=x1
			bar=y1
			y1 = y1 + self.stepX
			col.sat = col.sat - self.stepColor
			for j in range(0, self.aosY - 1):
				foo = foo + self.stepX
				bar = bar - self.stepY
				col.hue = col.hue + self.stepColor
				if (j > self.hue) :
					self.everyObj.append(w.create_rectangle(foo, bar, foo + self.sizeX, bar + self.sizeY, fill=col.toHex(), width=0))				
				
def parseToInt(string):
	num = False
	result = ""
	for i in string:
		if i.isdigit():
			result += i
			num = True
		elif num:
			return int(result)
	if result == "":
		result = 0
	return int(result)

#print(parseToInt("asd123a4sd"))	
