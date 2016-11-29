#!/usr/bin/env python3

#NOTE: To change explosion animation change desired class name of explosion to "Explosion"
#		instead of "Explosion1"
#Usage: Click on screen to start explsion at point of click , can click multiple times


import curses , curses.panel  
import time 
import random

class Animation():
	
	def __init__(self, y , x , fpa , drawOrder):
		self.frameCount = 0 
		self.fpa = fpa
		self.frRemToDraw = fpa
		self.window = curses.newwin(Explosion.panHeight , Explosion.panWidth , y , x)
		self.panel = curses.panel.new_panel(self.window)
		self.currentDraw = 0
		self.drawOrder = drawOrder
		self.lastDrawIndex = len(self.drawOrder) - 1
		if(not self.panel.hidden()): self.panel.hide()
	
	def move(self , x , y):
		self.panel.move(y , x)
		
	def setStartFrame(self , curFrame):
		self.startFrame = curFrame
		self.curFrame = curFrame
		
	def draw(self , newFrame):

		if(self.frRemToDraw > 0):
			if((self.currentDraw == 0) and (self.frRemToDraw == self.fpa)):
				self.panel.show()
			self.drawOrder[self.currentDraw]()
		else:
			if(self.currentDraw < self.lastDrawIndex):
				self.drawOrder[self.currentDraw]()
				self.currentDraw += 1
				self.frRemToDraw = self.fpa
				
			else:
				self.currentDraw = 0
				
		if(self.curFrame < newFrame):
			self.frRemToDraw -= 1
			self.curFrame += 1
	

class Explosion1(Animation):
	panWidth = 5
	panHeight = 5
	
	def __init__(self, y , x , fpa):
		drawOrder = [self.draw0 , self.draw1 , self.draw2 , self.draw2 , self.draw3]
		super(Explosion , self).__init__(y , x , fpa , drawOrder)

	def draw0(self):
		self.window.erase()
		self.window.addch(2 , 3 , '@' , curses.color_pair(2))		

	def draw1(self):
		self.window.erase()
		self.window.addch(1 , 3 , '#' , curses.color_pair(2))
		self.window.addch(2 , 2 , '#' , curses.color_pair(2))
		self.window.addch(2 , 3 , '@' , curses.color_pair(1))
		self.window.addch(2 , 4 , '#' , curses.color_pair(2))
		self.window.addch(3 , 3 , '#' , curses.color_pair(2))
  	
	def draw2(self):
		self.window.erase()
		self.window.addch(0 , 3 , '@' , curses.color_pair(2))
		self.window.addch(1 , 2 , '@' , curses.color_pair(2))
		self.window.addch(1 , 3 , '#' , curses.color_pair(1))
		self.window.addch(1 , 4 , '@' , curses.color_pair(2))
		self.window.addch(2 , 2 , '#' , curses.color_pair(1))
		self.window.addch(2 , 3 , '@' , curses.color_pair(2))
		self.window.addch(2 , 4 , '#' , curses.color_pair(1))
		self.window.addch(3 , 2 , '@' , curses.color_pair(2))
		self.window.addch(3 , 3 , '#' , curses.color_pair(1))
		self.window.addch(3 , 4 , '@' , curses.color_pair(2))
		self.window.addch(4 , 3 , '@' , curses.color_pair(2))
		
	def draw3(self):
		self.window.erase()
		self.window.addch(0 , 3 , '*' , curses.color_pair(3))
		self.window.addch(1 , 2 , '*' , curses.color_pair(3))
		self.window.addch(1 , 3 , '*' , curses.color_pair(4))
		self.window.addch(1 , 4 , '*' , curses.color_pair(3))
		self.window.addch(2 , 2 , '*' , curses.color_pair(4))
		self.window.addch(2 , 3 , '*' , curses.color_pair(3))
		self.window.addch(2 , 4 , '*' , curses.color_pair(4))
		self.window.addch(3 , 2 , '*' , curses.color_pair(3))
		self.window.addch(3 , 3 , '*' , curses.color_pair(4))
		self.window.addch(3 , 4 , '*' , curses.color_pair(3))
		self.window.addch(4 , 3 , '*' , curses.color_pair(3))
		
		
	
	
class Explosion(Animation):
	panWidth = 9
	panHeight = 9
	
	def __init__(self, y , x , fpa):
		drawOrder = [self.draw0 , self.draw1 , self.draw2 , 
					 self.draw3 , self.draw4 , self.draw3 , 
					 self.draw2 , self.draw1 , self.draw0]
		super(Explosion , self).__init__(y , x , fpa , drawOrder)

	def draw0(self):
		self.window.erase()
		self.window.addch(4 , 4 , '@' , curses.color_pair(2))		

	def draw1(self):
		self.window.erase()
		self.window.addch(3 , 4 , '#' , curses.color_pair(2))
		self.window.addch(4 , 3 , '#' , curses.color_pair(2))
		self.window.addch(4 , 4 , '@' , curses.color_pair(1))
		self.window.addch(4 , 5 , '#' , curses.color_pair(2))
		self.window.addch(5 , 4 , '#' , curses.color_pair(2))
  	
	def draw2(self):
		self.window.erase()
		self.window.addch(2 , 4 , '@' , curses.color_pair(2))
		self.window.addch(3 , 3 , '@' , curses.color_pair(2))
		self.window.addch(3 , 4 , '#' , curses.color_pair(1))
		self.window.addch(3 , 5 , '@' , curses.color_pair(2))
		self.window.addch(4 , 2 , '@' , curses.color_pair(2))
		self.window.addch(4 , 3 , '#' , curses.color_pair(1))
		self.window.addch(4 , 4 , '@' , curses.color_pair(2))
		self.window.addch(4 , 5 , '#' , curses.color_pair(1))
		self.window.addch(4 , 6 , '@' , curses.color_pair(2))
		self.window.addch(5 , 3 , '@' , curses.color_pair(2))
		self.window.addch(5 , 4 , '#' , curses.color_pair(1))
		self.window.addch(5 , 5 , '@' , curses.color_pair(2))
		self.window.addch(6 , 4 , '@' , curses.color_pair(2))

	def draw3(self):
		self.window.erase()
		self.window.addch(2 , 3 , '#' , curses.color_pair(1))
		self.window.addch(2 , 4 , '@' , curses.color_pair(2))
		self.window.addch(2 , 5 , '#' , curses.color_pair(1))
		self.window.addch(3 , 2 , '#' , curses.color_pair(1))
		self.window.addch(3 , 3 , '@' , curses.color_pair(2))
		self.window.addch(3 , 4 , '#' , curses.color_pair(1))
		self.window.addch(3 , 5 , '@' , curses.color_pair(2))
		self.window.addch(3 , 6 , '#' , curses.color_pair(1))
		self.window.addch(7 , 4 , '#' , curses.color_pair(1))
		self.window.addch(1 , 4 , '#' , curses.color_pair(1))
		self.window.addch(4 , 1 , '#' , curses.color_pair(1))
		self.window.addch(4 , 2 , '@' , curses.color_pair(2))
		self.window.addch(4 , 3 , '#' , curses.color_pair(1))
		self.window.addch(4 , 4 , '@' , curses.color_pair(2))
		self.window.addch(4 , 5 , '#' , curses.color_pair(1))
		self.window.addch(4 , 6 , '@' , curses.color_pair(2))
		self.window.addch(4 , 7 , '#' , curses.color_pair(1))
		self.window.addch(5 , 2 , '#' , curses.color_pair(1))
		self.window.addch(5 , 3 , '@' , curses.color_pair(2))
		self.window.addch(5 , 4 , '#' , curses.color_pair(1))
		self.window.addch(5 , 5 , '@' , curses.color_pair(2))
		self.window.addch(5 , 6 , '#' , curses.color_pair(1))
		self.window.addch(6 , 3 , '#' , curses.color_pair(1))
		self.window.addch(6 , 4 , '@' , curses.color_pair(2))
		self.window.addch(6 , 5 , '#' , curses.color_pair(1))
		
	def draw4(self):
		self.window.erase()
		self.window.addstr(2 , 0 , ' * *  * *' , curses.color_pair(4))
		self.window.addstr(3 , 0 , ' *      *' , curses.color_pair(4))
		self.window.addstr(4 , 0 , '    *' , curses.color_pair(4))
		self.window.addstr(5 , 0 , ' *      *' , curses.color_pair(4))
		self.window.addstr(6 , 0 , ' * *  * *' , curses.color_pair(4))

	
		
	

	

class GameLoop:
	
	def __init__(self):
		self.userInput = -1
		self.t = 0.0 
		self.dt = 0.02
		self.frameCount = 0
		self.eventLoc = None
	
	def startGame(self , stdscr):
		self.stdscr = stdscr
		self.stdscr.nodelay(1)
		
		self.max_y , self.max_x = stdscr.getmaxyx()
		self.configureCursesSettings()
		#self.exp = Explosion(int(self.max_y/2) - 10 , int(self.max_x/2) , 4)
		self.expList = [Explosion(0 , 0 , 5) for i in range(0, 10)]
		self.activeList = [] 
		
		self.runGameLoop()
		
	def processInput(self):
		self.userInput = self.stdscr.getch()
		if(self.userInput == curses.KEY_MOUSE):
			self.eventLoc = curses.getmouse()
			
	def addGameObject(self):
		e_x = self.eventLoc[1]
		e_y = self.eventLoc[2]
		exp = self.expList.pop()
		exp.setStartFrame(self.frameCount)
		exp.move(e_x , e_y)
		self.activeList.append(exp) 
			
	def configureCursesSettings(self):
		curses.init_pair(1 , curses.COLOR_RED , curses.COLOR_BLACK)
		curses.init_pair(2 , curses.COLOR_YELLOW , curses.COLOR_BLACK)
		curses.init_pair(3 , curses.COLOR_CYAN , curses.COLOR_BLACK)
		curses.init_pair(4 , curses.COLOR_WHITE , curses.COLOR_BLACK)
		curses.init_pair(5 , curses.COLOR_GREEN , curses.COLOR_BLACK)
		curses.curs_set(0)
		curses.mousemask(1)
		
		

	def runGameLoop(self):
		currentTime = time.perf_counter()
		lag = 0.02
		
		while(self.userInput != ord('q')):
		#process input--------------------------------------
			self.processInput()
		#Update loop----------------------------------------
			newTime = time.perf_counter()
			elapsedTime = newTime - currentTime
			currentTime = newTime
			lag += elapsedTime
			
			while(lag >= self.dt):
				#update()
				self.t += self.dt
				lag -= self.dt
				self.frameCount = self.frameCount + 1
				
		#render()-------------------------------------------
				
			self.stdscr.erase()
							
			if(self.eventLoc != None):
				self.addGameObject()
				self.eventLoc = None
			
			for p in self.activeList:
				p.draw(self.frameCount)

			
			curses.panel.update_panels()
			self.stdscr.refresh()
			
		curses.endwin()

gl = GameLoop()
curses.wrapper(gl.startGame)
