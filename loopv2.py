#!/usr/bin/env python3

import curses , curses.panel  
import time 
import random

#Make class abstract so it can't be instantiated (later)
class GameObject:
	def __init__(self , panH , panW):
		self.window = curses.newwin(panH , panW , 0 , 0)
		self.panel = curses.panel.new_panel(self.window)
		self.state = {'x' : 0.0 , 'y' : 0.0 , 'vx' : 0.0 , 'vy' : 0.0}

	def setXPos(self , x):
		self.state['x'] = x
		
	def setYPos(self , y):	
		self.state['y'] = y
		
	def setXYPos(self , x , y):
		setXPos(x)
		setYPos(Y)
		
	def setXVel(self , vx):
		self.state['vx'] = vx
		
	def setYVel(self , vy):
		self.state['vy'] = vy
				
	def getXPos(self):
		return self.state['x']

	def getYPos(self):
		return self.state['y']
		
	def getXYPos(self):
		return self.state['x'] , self.state['y']

	def getXVel(self):
		return self.state['vx']
		
	def getYVel(self):
		return self.state['vy']
		
	def getXYVel(self):
		return self.state['vx'] , self.state['vy']
		
	def setState(self , x , y , vx , vy):
		setXPos(x)
		setYPos(y)
		setXVel(vx)
		setYVel(vy)

	def movePos(self):
		self.astPan.move(int(self.state['y']) , int(self.state['x']))
		
	def boundaryCheck(self , max_x , max_y):  
		if(self.state['y'] < 0):
			return True
		elif(self.state['y'] + self.astWin.getyx()[0] >= max_y):
			return True
		elif(self.state['x'] < 0):
			return True
		elif(self.state['x'] + self.astWin.getmaxyx()[1] >= max_x):
			return True
		return False

class Spaceship():
	
	def __init__(self , x , y):
		self.x = x
		self.y = y
		self.shipWin = curses.newwin(5 , 7 , y , x)
		self.shipPan = curses.panel.new_panel(self.shipWin)
		 
	def updatePos(self , q , max_x , max_y):
		if(q == ord('w') and self.y > 0):
			self.y -= 1
		elif(q == ord('s') and self.y < max_y - self.shipWin.getmaxyx()[0]):
			self.y += 1
		elif(q == ord('a') and self.x > 0):
			self.x -= 1
		elif(q == ord('d') and self.x < max_x - self.shipWin.getmaxyx()[1]):
			self.x += 1
		self.shipPan.move(self.y , self.x)
	
	def drawShip(self):	
		self.shipWin.addstr(0 , 0 , '  /^\\ ' , curses.color_pair(1));
		self.shipWin.addstr(1 , 0 , ' ||_|| ' , curses.color_pair(1));
		self.shipWin.addstr(2 , 0 , '< /_\\ >' , curses.color_pair(1));
		self.shipWin.addstr(3 , 0 , ' ^^^^^ ' , curses.color_pair(2));		

class Asteroid(GameObject):
	panWidth = 4
	panHeight = 4
	
	def __init__(self):
			super().__init__(Asteroid.panHeight , Asteroid.panWidth)
			
	def draw(self):		
		self.astWin.addstr(0 , 0 , '/Oo\\' , curses.color_pair(3))
		self.astWin.addstr(1 , 0 , 'OO0o' , curses.color_pair(3))
		self.astWin.addstr(2 , 0 , '\\0o/ ' , curses.color_pair(3))
		
#WORKING ON THIS RIGHT NOW (10/26/2016)	-------------------------------------------------------	
class GameObjectLogic():
	
	def __init__(self , max_x , max_y):
		self.max_x = max_x
		self.max_y = max_y
		self.gameObjsDict = {}
	
	def createGameObjs(self , parentClass):
		gameObjClassNames = [c.__name__ for c in parentClass.__subclasses__()]
		
		for cNameStr in gameObjClassNames:
			self.gameObjsDict[cNameStr] = {"active" : [] , "inactive" : []}
			clazz = globals()[cNameStr]
			numObjsToFillScr = (self.max_x // clazz.panWidth)
			self.gameObjsDict[cNameStr]['numObjs'] = numObjsToFillScr 
			for i in range(0 , numObjsToFillScr): #prob change this calc
				self.gameObjsDict[cNameStr]["inactive"].append(clazz())
		
	#scalePercent:
		#float between [0 , 1]
		#defines the percentage of the width
		#of the screen that will intially  
		#be populated with game objects 	
	def intialSpawn(self , gameObj , scalePercent):
		pass

#w = curses.initscr()
#gol = GameObjectLogic(12 , 12)
#gol.createGameObjs(GameObject)
#print(gol.gameObjsDict)
#curses.endwin()
#-----------------------------------------------------------------------------------------------

#WORKING ON THIS RIGHT NOW (10/26/2016)		
#class PhysicsEngine():
#	
#	def __init__(self , GameObjects , max_x , max_y):
#		self.max_x = max_x
#		self.max_y = max_y
#		self.numAsteroids = int(max_x // GameObjects.panWidth)
#		self.gObjList = []
#		
#		for i in range(self.numAsteroids * 2):
#			#((i % self.numAsteroids) * GameObject.panWidth)  + 1
#			newWindow = curses.newwin(GameObjects.panHeight , GameObjects.panWidth , 0 , 0)
#			newPanel = curses.panel.new_panel(newWindow)
#			newAst = Asteroid(newWindow , newPanel)
#			#GameLoop.activeGOList.append(newAst)
#			self.gObjList.append(newAst)
#	
#	def applyKinematics(self , gameObj , updateTimeDelta):
#		gameObj.state['x'] += (gameObj.state['vx'] * updateTimeDelta)
#		gameObj.state['y'] += (gameObj.state['vy'] * updateTimeDelta)	
#			
#	def getGameObjects(self):
#		return self.gObjList
#			
#	def runPhysics(self , activeObjects , ss):
#		for o in activeObjects:
#			pass
#				
#	def checkForCollision(self , ss , obj):
#		if(obj.astWin.enclose(ss.y , ss.x)):
#			pass
#------------------------------------------------------------------------------------------------
		

class GameLoop:
	
	def __init__(self):
		self.userInput = -1
		#Elapsed Game time
		self.t = 0.0 
		#Time in milliseconds between frame render 
		#Frame renders every 20ms (50 FPS)
		self.dt = 0.02 
		
	def startGame(self , stdscr):
		self.stdscr = stdscr
		self.stdscr.nodelay(1)
		self.max_y , self.max_x = stdscr.getmaxyx()
		self.configureCursesSettings()
		self.createPlayer()
		self.runGameLoop()
	
	def configureCursesSettings(self):
		curses.init_pair(1 , curses.COLOR_RED , curses.COLOR_BLACK)
		curses.init_pair(2 , curses.COLOR_YELLOW , curses.COLOR_BLACK)
		curses.init_pair(3 , curses.COLOR_CYAN , curses.COLOR_BLACK)
		curses.curs_set(0)
		
	def createPlayer(self):
		self.spaceShip = Spaceship(int(self.max_x/2) , int(self.max_y/2))
		
	def processInput(self):
		self.userInput = self.stdscr.getch()
		self.spaceShip.updatePos(self.userInput , self.max_x , self.max_y)
		
	def update(self):
		pass

	def render(self):
		self.stdscr.erase()
		self.spaceShip.drawShip()	
		curses.panel.update_panels()
		self.stdscr.refresh()	
	
	def runGameLoop(self):
		currentTime = time.perf_counter()
		lag = 0.0								
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
				
		#render()-------------------------------------------
			self.render()
		
		curses.endwin()
		
gl = GameLoop()
curses.wrapper(gl.startGame)   

