# This file provides the runtime support for running a basic program
# Assumes the program has been parsed using basparse.py

import sys
import math
import random

class MyInterpreter:
	
	# Initialize the interpreter. prog is a dictionary
	# containing (line,statement) mappings
	def __init__(self, prog):
		self.prog= prog

		self.functions = {           # Built-in function table
			'INT': lambda z: int(self.eval(z)),
			'RND': lambda z: random.random()
		}
		

	# Collecting all data statements
	def collect_data(self):
		self.data = []
		for lineno in self.stat:
			if self.prog[lineno][0] == 'DATA':
				self.data = self.data + self.prog[lineno][1]
		self.dc = 0                  # Initialize the data counter


	# Check for start statements
	def check_start(self):
		has_application = -1
		for lineno in self.stat:
			if self.prog[lineno][0] == 'APPLICATION':
				has_application = lineno
		if has_application != 0:
			print("ERROR:	NO START INSTRUCTION")
			self.error = 1
			return 


	# Checking finish statement in the prog
	def check_finish(self):
		has_end = 0
		for lineno in self.stat:
			if self.prog[lineno][0] == 'FINISH' and not has_end:
				has_end = lineno
		if not has_end:
			print("ERROR:	NO FINISH INSTRUCTION")
			self.error = 1
			return
		if has_end != lineno:
			print("ERROR:	FINISH IS NOT LAST")
			self.error = 1


	#Creating a robot
	def create_robot(self, cord1, cord2):
		self.robot.append(cord1)
		self.robot.append(cord2)
		self.robot.append('RIGHT')
		self.path.append((cord1, cord2))
		self.sc.append(self.cells[cord1][cord2])
		self.sc.append(self.cells[cord1][cord2])
		self.cells[cord1][cord2] = 'R'


	#Creating a cell
	def create_cell(self):
		temp = ['*'] * 7
		v = []
		for i in range(7):
			v.append(temp[:])
		self.cells = v
		labirinth = (
		('0', '0', '0', '0', '0'), ('|', '0', '|', '0', '0'), ('0', '|', '0', 'E', '0'), ('0', '0', '0', '0', '0'),
		('0', '0', '|', '0', '0'))
		#('0', '?', '?', '%', '~'), ('|', '@', '0', '0', '0'), ('~', '|', '0', '0', '0'), ('0', '@', '|', '|', '0'),
		#('+', '@', '+', '0', 'E')
		for i in range(len(labirinth)):
			for j in range(len(labirinth[i])):
				if labirinth[i][j] == '0':
					self.cells[i + 1][j + 1] = '0'
				elif labirinth[i][j] == '|':
					self.cells[i + 1][j + 1] = '|'
				elif labirinth[i][j] == 'E':
					self.cells[i + 1][j + 1] = 'E'
				elif labirinth[i][j] == '*':
					self.cells[i + 1][j + 1] = '*'
				elif labirinth[i][j] == '$':
					self.cells[i + 1][j + 1] = '$'
				elif labirinth[i][j] == '+':
					self.cells[i + 1][j + 1] = '+'
				elif labirinth[i][j] == '~':
					self.cells[i + 1][j + 1] = '~'
				elif labirinth[i][j] == '@':
					self.cells[i + 1][j + 1] = '@'
				elif labirinth[i][j] == '%':
					self.cells[i + 1][j + 1] = '%'
				elif labirinth[i][j] == '?':
					self.cells[i + 1][j + 1] = '?'


	# Creating a list of walls (special materials)
	def create_walls(self):
		d = {
		"$": 60,        #steel
		"~": 10,        #plastic 
		"+": 20,        #glass  
		"@": 40,        #concrete
		"%": 110,       #steel-glass-plastic-glass
		"?": 30,        #plastic-glass
		"|": 5  		#regular wall
		}   
		self.walls.update(d)
   

	#Printing a cell
	def print_cell(self):
		i = 0
		j = 0
		for i in range(len(self.cells)):
			print self.cells[i][0],self.cells[i][1],self.cells[i][2],self.cells[i][3],self.cells[i][4],self.cells[i][5],self.cells[i][6]
		print " "


	#Going forward
	def forward(self):
		walls = ['?', '@', '%', '+', '*', '$', '~', '|']
		if self.robot[2] == 'RIGHT':
			cord1 = self.robot[0]
			cord2 =  self.robot[1]
			if self.cells[cord1][cord2 + 1] not in walls:
				self.sc[1] = self.cells[cord1][cord2 + 1]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1][cord2 + 1] = 'R'
				self.robot[1] = self.robot[1] + 1   
				print("\nright - go_forward")
				return True
			else:
				print("right - go_forward")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False
		elif self.robot[2] == 'LEFT':
			cord1 = self.robot[0]
			cord2 =  self.robot[1]
			if self.cells[cord1][cord2 - 1] not in walls:
				self.sc[1] = self.cells[cord1][cord2 - 1]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1][cord2 - 1] = 'R'
				self.robot[1] = self.robot[1] - 1     
				print("left - go_forward")
				return True
			else:
				print("left - go_forward")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False
		elif self.robot[2] == 'FORWARD':
			cord1 = self.robot[0]
			cord2 =  self.robot[1]
			if self.cells[cord1 - 1][cord2] not in walls:
				self.sc[1] = self.cells[cord1 -1][cord2]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1 - 1][cord2] = 'R'
				self.robot[0] = self.robot[0] - 1    
				print("forward - go_forward")
				return True
			else:
				print("forward - go_forward")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False
		elif self.robot[2] == 'BACK':
			cord1 = self.robot[0]
			cord2 =  self.robot[1]
			if self.cells[cord1 + 1][cord2] not in walls:
				self.sc[1] = self.cells[cord1 + 1][cord2]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1 + 1][cord2] = 'R'
				self.robot[0] = self.robot[0] + 1   
				print("back - go_forward")
				return True
			else:
				print("back - go_forward")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False


	#Going backwards
	def back(self):
		walls = ['?', '@', '%', '+', '*', '$', '~', '|']
		if self.robot[2] == 'RIGHT':
			cord1 = self.robot[0]
			cord2 =  self.robot[1]
			if self.cells[cord1][self.robot[1] - 1] not in walls:
				self.sc[1] = self.cells[cord1][cord2 - 1]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1][cord2 - 1] = 'R'
				self.robot[1] = self.robot[1] - 1
				print("right - go_back")
				return True
			else:
				print("right - go_back")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False
		elif self.robot[2] == 'LEFT':
			cord1 = self.robot[0]
			cord2 =  self.robot[1]
			if self.cells[cord1][cord2 + 1] not in walls:
				self.sc[1] = self.cells[cord1][cord2 + 1]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1][cord2 + 1] = 'R'
				self.robot[1] = self.robot[1] + 1
				print("left - go_back")
				return True
			else:
				print("left - go_back")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False
		elif self.robot[2] == 'FORWARD':
			cord1 = self.robot[0]
			cord2 = self.robot[1]
			if self.cells[cord1 + 1][cord2] not in walls:
				self.sc[1] = self.cells[cord1 + 1][cord2]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1 + 1][cord2] = 'R'
				self.robot[0] = self.robot[0] + 1
				print("forward - go_back")
				return True
			else:
				print("forward - go_back")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False
		elif self.robot[2] == 'BACK':
			cord1 = self.robot[0]
			cord2 = self.robot[1]
			if self.cells[cord1 - 1][cord2] not in walls:
				self.sc[1] = self.cells[cord1 + 1][cord2]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1 - 1][cord2] = 'R'
				self.robot[0] = self.robot[0] - 1
				print("back - go_back")
				return True
			else:
				print("back - go_back")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False
		

	#Going to the right side
	def right(self):
		walls = ['?', '@', '%', '+', '*', '$', '~', '|']
		if self.robot[2] == 'RIGHT':
			cord1 = self.robot[0]
			cord2 =  self.robot[1]
			if self.cells[cord1 + 1][cord2] not in walls:
				self.sc[1] = self.cells[cord1 + 1][cord2]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1 + 1][cord2] = 'R'
				self.robot[0] = self.robot[0] + 1
				print("right - go_right")
				return True
			else:
				print("right - go_right")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False
		elif self.robot[2] == 'LEFT':
			cord1 = self.robot[0]
			cord2 =  self.robot[1]
			if self.cells[cord1 - 1][cord2] not in walls:
				self.sc[1] = self.cells[cord1 - 1][cord2]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1 - 1][cord2] = 'R'
				self.robot[0] = self.robot[0] - 1
				print("left - go_right")
				return True
			else:
				print("left - go_right")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False
		elif self.robot[2] == 'FORWARD':
			cord1 = self.robot[0]
			cord2 = self.robot[1]
			if self.cells[cord1][cord2 + 1] not in walls:
				self.sc[1] = self.cells[cord1][cord2 + 1]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1][cord2 + 1] = 'R'
				self.robot[1] = self.robot[1] + 1
				print("forward - go_right")
				return True
			else:
				print("forward - go_right")             
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False
		elif self.robot[2] == 'BACK':
			cord1 = self.robot[0]
			cord2 = self.robot[1]
			if self.cells[cord1][cord2 + 1] not in walls:
				self.sc[1] = self.cells[cord1][cord2 - 1]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1][cord2 + 1] = 'R'
				self.robot[1] = self.robot[1] + 1
				print("back - go_right")
				return True
			else:
				print("back - go_right")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False


	#Going to the left side
	def left(self):
		walls = ['?', '@', '%', '+', '*', '$', '~', '|']
		if self.robot[2] == 'RIGHT':
			cord1 = self.robot[0]
			cord2 =  self.robot[1]
			if self.cells[cord1 - 1][cord2] not in walls:
				self.sc[1] = self.cells[cord1 - 1][cord2]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1 - 1][cord2] = 'R'
				self.robot[0] = self.robot[0] - 1
				print("right - go_left")
				return True
			else:
				print("right - go_left")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False
		elif self.robot[2] == 'LEFT':
			cord1 = self.robot[0]
			cord2 =  self.robot[1]
			if self.cells[cord1 + 1][cord2] not in walls:
				self.sc[1] = self.cells[cord1 + 1][cord2]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1 + 1][cord2] = 'R'
				self.robot[0] = self.robot[0] + 1
				print("left - go_left")
				return True
			else:
				print("left - go_left")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False
		elif self.robot[2] == 'FORWARD':
			cord1 = self.robot[0]
			cord2 = self.robot[1]
			if self.cells[cord1][cord2 - 1] not in walls:
				self.sc[1] = self.cells[cord1][cord2 - 1]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1][cord2 - 1] = 'R'
				self.robot[1] = self.robot[1] - 1
				print("forward - go_left")
				return True
			else:
				print("forward - go_left")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False
		elif self.robot[2] == 'BACK':
			cord1 = self.robot[0]
			cord2 = self.robot[1]
			if self.cells[cord1][cord2 - 1] not in walls:
				self.sc[1] = self.cells[cord1][cord2 - 1]
				self.cells[cord1][cord2] = self.sc[0]
				self.sc[0] = self.sc[1]
				self.cells[cord1][cord2 - 1] = 'R'
				self.robot[1] = self.robot[1] - 1
				print("back - go_left")
				return True
			else:
				print("back - go_left")
				print("ERROR:	ROBOT CANNOT GO THIS WAY, TURN THE OTHER WAY OR DRILL THE WALL\n")
				return False


	#Function which defines the rotation to the left side
	def rotate_left(self):   
		if self.robot[2] == 'RIGHT':        #now
			self.robot[2] = 'FORWARD'       #then
			print ("turn: right->forward")
		elif self.robot[2] == 'FORWARD':
			self.robot[2] = 'LEFT'
			print ("turn: forward->left")
		elif self.robot[2] == 'LEFT':
			self.robot[2] = 'BACK'
			print("turn: left->back")
		elif self.robot[2] == 'BACK':
			self.robot[2] = 'RIGHT'
			print("turn: back->right")
		return True


	#Function which defines the rotation to the right side
	def rotate_right(self):
		if self.robot[2] == 'RIGHT':
			self.robot[2] = 'BACK'
			print ("turn: right->back")
		elif self.robot[2] == 'BACK':
			self.robot[2] == 'LEFT'
			print ("turn: back->left")
		elif self.robot[2] == 'LEFT':
			self.robot[2] = 'FORWARD'
			print ("turn: left->forward")
		elif self.robot[2] == 'FORWARD':
			self.robot[2] = 'RIGHT'
			print ("turn: forward->right")
		return True


	#Check finish cell in the labyrinth
	def check_finish_in_lab(self):
		if self.sc[0] == 'E':
			print("++++		ROBOT FOUND EXIT FROM LABIRINTH AWESOME!!!		++++")
			return 1


	#This is how my radar is working
	def lms(self):
		walls = ['?', '@', '%', '+', '*', '$', '~', '|']
		if self.robot[2] == 'RIGHT':   
			x = self.robot[0]
			y = self.robot[1]
			counter = 0
			for i in range(y, len(self.cells[x])):
				if self.cells[x][i] in walls:
					print 'To the nearest wall in this direction--> ', counter
					self.lms_var = counter;
					return 0
				counter = counter + 1   

		elif self.robot[2] == 'LEFT':       
			x = self.robot[0]
			y = self.robot[1]
			counter = 0
			rev_list = []
			for item in reversed(self.cells[x]):
				rev_list.append(str(item))
			k = rev_list.index('R') 
			for i in range(k, len(rev_list)):
				if rev_list[i] in walls:
					print 'To the nearest wall in this direction--> ', counter
					self.lms_var = counter;
					return 0
				counter = counter + 1

		elif self.robot[2] == 'FORWARD': 
			x = self.robot[0]
			y = self.robot[1]
			counter = 0
			rev_list = []
			good_list = []
			for item in range(len(self.cells[x])):
				rev_list.append(self.cells[item][y])
			for item in reversed(rev_list):
				good_list.append(str(item))
			k = good_list.index('R')    
			for i in range(k, len(good_list)):
				if good_list[i] in walls:
					print 'To the nearest wall in this direction--> ', counter
					self.lms_var = counter;
					return 0
				counter = counter + 1

		elif self.robot[2] == 'BACK':   
			x = self.robot[0]
			y = self.robot[1]
			counter = 0
			for i in range(x, len(self.cells[x])):
				if self.cells[i][y] in walls:
					print  'To the nearest wall in this direction--> ', counter
					self.lms_var = counter;
					return 0
				counter = counter + 1


	#Defining the material of the wall
	def reflect(self):
		if self.robot[2] == 'RIGHT':
			x = self.robot[0]
			y = self.robot[1]
			if self.cells[x][y+1] == '|':
				print('WALL\n')
				return 0
			elif self.cells[x][y+1] == '*':
				print('UNDEF\n')
				return 0
			elif self.cells[x][y+1] == '$':
				print('STEEL\n')
				return 0
			elif self.cells[x][y+1] == '~':
				print('PLASTIC\n')
				return 0
			elif self.cells[x][y+1] == '+':
				print('GLASS\n')
				return 0
			elif self.cells[x][y+1] == '@':
				print('CONCRETE\n')
				return 0
			elif self.cells[x][y+1] == '%':
				print('STEEL-GLASS-PLASTIC-GLASS\n')
				return 0
			elif self.cells[x][y+1] == '?':
				print('PLASTIC-GLASS\n')
				return 0
			elif self.cells[x][y+1] in self.walls.keys():
				print('SOME KIND OF WALL\n')
				return 0
		elif self.robot[2] == 'LEFT':
			x = self.robot[0]
			y = self.robot[1]
			if self.cells[x][y-1] == '|' :
				print('WALL\n')
				return 0
			elif self.cells[x][y-1] == '*':
				print('UNDEF\n')
				return 0
			elif self.cells[x][y-1] == '$':
				print('STEEL\n')
				return 0
			elif self.cells[x][y-1] == '~':
				print('PLASTIC\n')
				return 0
			elif self.cells[x][y-1] == '+':
				print('GLASS\n')
				return 0
			elif self.cells[x][y-1] == '@':
				print('CONCRETE\n')
				return 0
			elif self.cells[x][y-1] == '%':
				print('STEEL-GLASS-PLASTIC-GLASS\n')
				return 0
			elif self.cells[x][y-1] == '?':
				print('PLASTIC-GLASS\n')
				return 0
			elif self.cells[x][y-1] in self.walls.keys():
				print('SOME KIND OF WALL\n')
				return 0
		elif self.robot[2] == 'FORWARD':
			x = self.robot[0]
			y = self.robot[1]
			if self.cells[x-1][y] == '|' :
				print('WALL\n')
				return 0
			elif self.cells[x-1][y] == '*':
				print('UNDEF\n')
				return 0
			elif self.cells[x-1][y] == '$':
				print('STEEL\n')
				return 0
			elif self.cells[x-1][y] == '~':
				print('PLASTIC\n')
				return 0
			elif self.cells[x-1][y] == '+':
				print('GLASS\n')
				return 0
			elif self.cells[x-1][y] == '@':
				print('CONCRETE\n')
				return 0
			elif self.cells[x-1][y] == '%':
				print('STEEL-GLASS-PLASTIC-GLASS\n')
				return 0
			elif self.cells[x-1][y] == '?':
				print('PLASTIC-GLASS\n')
				return 0
			elif self.cells[x-1][y] in self.walls.keys():
				print('SOME KIND OF WALL\n')
				return 0
		elif self.robot[2] == 'BACK':
			x = self.robot[0]
			y = self.robot[1]
			if self.cells[x+1][y] == '|' :
				print('WALL\n')
				return 0
			elif self.cells[x+1][y] == '*':
				print('UNDEF\n')
				return 0
			elif self.cells[x+1][y] == '$':
				print('STEEL\n')
				return 0
			elif self.cells[x+1][y] == '~':
				print('PLASTIC\n')
				return 0
			elif self.cells[x+1][y] == '+':
				print('GLASS\n')
				return 0
			elif self.cells[x+1][y] == '@':
				print('CONCRETE\n')
				return 0
			elif self.cells[x+1][y] == '%':
				print('STEEL-GLASS-PLASTIC-GLASS\n')
				return 0
			elif self.cells[x+1][y] == '?':
				print('PLASTIC-GLASS\n')
				return 0
			elif self.cells[x+1][y] in self.walls.keys():
				print('SOME KIND OF WALL\n')
				return 0


	# Drilling the wall in the labyrinth
	def drill(self):
		if self.robot[2] == 'RIGHT':
			cord1 = self.robot[0]
			cord2 = self.robot[1]
			print("right - drill")
			if self.cells[cord1][cord2 + 1] == '*':
				print("ERROR:	ROBOT CANNOT DESTROY THIS WALL, TURN THE OTHER WAY\n")
			elif self.cells[cord1][cord2 + 1] in self.walls:
				wall = self.cells[cord1][cord2 + 1]
				k = self.walls[wall]
				if k < self.drill_cap:
					self.cells[cord1][cord2 + 1] = '0'
					self.drill_cap = self.drill_cap - k 
				else:
					print("ERROR:	ROBOT CANNOT DESTROY THIS WALL, TURN THE OTHER WAY\n")
					self.drill_cap = 0
			else:
				print("ERROR:	ROBOT DOESNT KNOW WHAT TO DESTROY")  
				
		elif self.robot[2] == 'LEFT':
			cord1 = self.robot[0]
			cord2 = self.robot[1] 
			print("left - drill")
			if self.cells[cord1][cord2 - 1] == '*':
				print("ERROR:	ROBOT CANNOT DESTROY THIS WALL, TURN THE OTHER WAY\n")
			elif self.cells[cord1][cord2 - 1] in self.walls:
				wall = self.cells[cord1][cord2 - 1]
				k = self.walls[wall]
				if k < self.drill_cap:
					self.cells[cord1][cord2 - 1] = 0 
					self.drill_cap = self.drill_cap - k
				else:
					print("ERROR:	ROBOT CANNOT DESTROY THIS WALL, TURN THE OTHER WAY\n")
					self.drill_cap = 0
			else:
				print("ERROR:	ROBOT DOESNT KNOW WHAT TO DESTROY")

		elif self.robot[2] == 'FORWARD':
			cord1 = self.robot[0]
			cord2 =  self.robot[1]
			print("forward - drill")
			if self.cells[cord1 - 1][cord2] == '*':
				print("ERROR:	ROBOT CANNOT DESTROY THIS WALL, TURN THE OTHER WAY\n") 
			elif self.cells[cord1 - 1][cord2] in self.walls:
				wall = self.cells[cord1 - 1][cord2]
				k = self.walls[wall]
				if k <= self.drill_cap:
					self.cells[cord1 -1][cord2] = 0  
					self.drill_cap = self.drill_cap - k
				else:
					print("ERROR:	ROBOT CANNOT DESTROY THIS WALL, TURN THE OTHER WAY\n")
					self.drill_cap = 0
			else:
				print("ERROR:	ROBOT DOESNT KNOW WHAT TO DESTROY")  

		elif self.robot[2] == 'BACK':
			cord1 = self.robot[0]
			cord2 =  self.robot[1]
			print("back - drill")
			if self.cells[cord1 + 1][cord2] == '*':
				print("ERROR:	ROBOT CANNOT DESTROY THIS WALL, TURN THE OTHER WAY\n")
			elif self.cells[cord1 + 1][cord2] in self.walls:
				wall = self.cells[cord1 + 1][cord2]
				k = self.walls[wall]
				if k < self.drill_cap:
					self.cells[cord1 + 1][cord2] = 0
					self.drill_cap = self.drill_cap - k
				else:
					print("ERROR:	ROBOT CANNOT DESTROY THIS WALL, TURN THE OTHER WAY\n")
					self.drill_cap = 0
			else:
				print("ERROR:	ROBOT DOESNT KNOW WHAT TO DESTROY")

		print 'CAPACITY OF DRILL: ', self.drill_cap
		print '\n'


	#Evaluate an expression
	def eval(self, expr):
		iter_var = 0
		spisok = ['NUM', 'STR', 'BOOL', 'TRUE', 'FALSE', 'UNDEFINED', 'BINOP']
		if type(expr) == int:
			return expr
		expr_type = expr[0]
		if expr_type in spisok:	
			if expr_type == 'NUM':
				return expr[1]
			elif expr_type == 'STR':
				return expr[1]
			elif expr_type == 'BOOL':
				return expr[1]
			elif expr_type == 'TRUE':
				return expr[1]
			elif expr_type == 'FALSE':
				return expr[1]
			elif expr_type == 'UNDEFINED':
				return expr[1]
			elif expr_type == 'UNARY':
				if expr[1] == '-':      
					return -self.eval(expr[2])
			elif expr_type == 'BINOP':
				if expr[1] == '+':
					eval1 = expr[2]
					eval2 = expr[3]
					b=[]
					if eval1[0] in self.vars or eval2[0] in self.vars:
						if eval1[0] in self.int or eval2[0] in self.int:
							if type(eval1) is str and type(eval2) is str:
								print ' '
							elif type(eval1[0]) is str and type(eval2[0]) is str:
								if eval1[0] in self.iter_var and eval2[0] in self.iter_var:
									first = self.iter_var[eval1[0]][0]
									second = self.iter_var[eval2[0]][0]
									iter_var = int(first)
									iter_var += int(second)
									b.append('NUM')
									b.append(iter_var)
									self.iter_var[eval1[0]] = b
									return b
							elif type(eval1[0]) is str and (type(eval2[0]) is int and eval2[1] == 'NUM'):
								if eval1[0] in self.iter_var:
									first = self.iter_var[eval1[0]][0]
									second = eval2[0]
									iter_var = int(first)
									iter_var += int(second)
									b.append('NUM')
									b.append(iter_var)
									self.iter_var[eval1[0]] = b
									return b
							elif (type(eval1[1]) is int or eval1[0] == 'NUM') and (type(eval2[1]) is int and eval2[0] == 'NUM'):
								iter_var = int(eval1[1])
								iter_var += int(eval2[1])
								b.append('NUM')
								b.append(iter_var)
								return b
							elif type(eval1[0]) is not int and (type(eval2[1]) is int or eval2[0] == 'NUM'):
								iter_var = int(self.vars[eval1[0]][0])
								iter_var += int(eval2[1])
								b.append('NUM')
								b.append(iter_var)
								return b
							elif (type(eval1[0]) is int or eval2[0] == 'NUM') and type(eval2[0]) is not int:
								iter_var = int(self.vars[eval2[0]][0])
								iter_var += int(eval1[1])
								b.append('NUM')
								b.append(iter_var)
								return b
						else:
							print ("ERROR:	  VARIABLES NOT FOUND")
							raise RuntimeError
				if expr[1] == '-':
					return self.eval(expr[2]) - self.eval(expr[3])
		else:
			print ' '


				
	# Evaluate a relational expression
	def releval(self, expr):
			signs = ['<', '>', '<>', '=']
			expr_type = expr[1]
			lhs = self.eval(expr[2][0])
			rhs = self.eval(expr[2][1])
			if lhs == None:
				lhs = expr[2][0][0]
				if lhs in self.vars:
					lhs = self.vars[expr[2][0][0]][0]
				else:
					print ("ERROR:	VARIABLE NOT FOUND")
					raise RuntimeError
			if rhs == None:     	
				rhs = expr[2][1][0]
				if rhs in self.vars:
					rhs = self.vars[expr[2][1][0]][0]
				else:
					print ("ERROR:	VARIABLE NOT FOUND")
					raise RuntimeError
			print 'In releval',lhs, expr_type, rhs
			if expr_type in signs:
				if expr_type == '<':
					if int(lhs) < int(rhs):
						return True
					else:
						return False
				elif expr_type == '>':
					if int(lhs) > int(rhs):
						return True
					else:
						return False
				elif expr_type == '=':
					if int(lhs) == int(rhs):
						return True
					else:
						return False
				elif expr_type == '<>':
					if int(lhs) != int(rhs):
						return True
					else:
						return False


	def assign_default(self, instr):
		i = len(self.func_args_iter)
		k = 0			# checking that the num of arguments is okay for continuing to work
		while k != i:
			var = self.func_args[k]
			s = []
			l = []
			s.append(instr[k])
			self.func_args_iter[k].append(instr[k])
			s.append('NUM')
			self.iter_var[var] = s
			k = k + 1
		if len(self.func_args_iter) < len(instr):
			p = len(instr) - len(self.func_args_iter)  # how many times it will go in cycle
			k = len(self.func_args_iter)   		       # pos from where to append
			while p != 0:
				var = instr[k]
				s = []
				s.append(var)
				s.append('NUM')
				self.rest_of_args.append(s)
				p = p - 1
				k = k + 1

	# Assignment
	def assign(self, target, value, types):
		i = len(target) 
		k = 0 
		while i != 0:
			var = target[k][0]
			s = []
			a = value
			s.append(a)
			s.append(types)
			if types == 'BOOLEAN':
				self.bool[var] = s
			elif types == 'INTEGER':
				self.int[var] = s
			elif types == 'STRING':
				self.str[var] = s
			self.vars[var] = s  # so we wont have same names of different variables
			i = i - 1
			k = k + 1


##########################################################################################


	def run(self):
		self.vars = {}          # all variables
		self.int = {}           # all int variables
		self.bool = {}          # all bool variables
		self.str = {}           # all string variables
		self.arrays = {}        # arrays variables
		self.tables = {}            # tables
		self.var = {}
		self.loops = []            # Currently active loops
		self.loopend = {}            # Mapping saying where loops end
		self.error = 0              # Indicates program error
		self.found = 0 				# Indicates that the robot found the way out
		self.func = {}
		self.path = []
		self.cord1 = 0
		self.cord2 = 0
		self.parameters = {}
		self.ret = 0
		self.lists = {}
		self.lms_var = 0 
		self.self_args = 0 
		self.iter_var = {}
		self.save_procedure = []
		self.save_args = []
		self.func_args = []
		self.func_args_iter = []
		self.rest_of_args = []
		self.func_ret = {}
		self.flag = 0

		self.stat = list(self.prog)  # Ordered list of all line numbers
		self.stat.sort()
		self.pc = 0                  # Current program counter
		self.robot = []
		self.walls = {}
		self.drill_cap = 70
		self.sc = []
		self.kol_args = 0 
		self.kol_args_in_func = 0 

		# Processing prior to running

		self.collect_data()          # Collect all of the data statements
		self.check_start()
		self.check_finish()
		self.create_walls()
		self.create_cell()

		if self.error:
			print 'ERROR:	SOMETHING WRONG...'
			raise RuntimeError

		while 1:
			line = self.stat[self.pc]
			instr = self.prog[line]
			self.ret = 0
			op = instr[0]

		#FINISH
			if op == 'FINISH':
				break;   # We are done
			
		# PRINT statement
			elif op == 'PRINT':
				plist = instr[1]
				out = ""
				if plist[0] in self.iter_var:
					for value in plist:
						evaling = self.iter_var[value]
						print evaling[0]
				elif plist[0] in self.vars:
					for value in plist:
						evaling = self.vars[value]
						print evaling[0]
				elif plist[0] in self.lists:
					print "\t"
					for el in self.lists[plist[0]]:
						print el[1], 
					print '\n'
				else:
					print ('ERROR:	CANNOT FIND THIS VARIABLE')  


		# VARIABLE DECLARATION statement
			if op == 'INTEGER':
				target = instr[1]
				value = 0
				self.assign(target, value, op)
			elif op == 'STRING':
				target = instr[1]
				value = ''
				self.assign(target, value, op)
			elif op == 'BOOLEAN':
				target = instr[1]
				value = 'UNDEFINED'
				self.assign(target, value, op)
			
		# ASSIGN statement
			if op == 'ASSIGN':
				target = instr[1][0]
				value = []
				value.append(instr[2][1])

				if instr[2][0] == None:
					print ("ERROR:	  WRONG ASSIGNMENT FOR STRING VARIABLE")
					raise RuntimeError
				value.append(instr[2][0])
				s = []

				if target in self.vars:
					if value[1] == 'BOOL' or value[1] == 'STR' or value[1] == 'NUM':
						s.append(target)
						s.append(value)
						if value[1] == 'BOOL' and target in self.bool:
							if value[0] == 'true' or value[0] == 'false':
								self.bool[target] = s[1]
								self.vars[target] = s[1]
								self.iter_var[target] = s[1]
							else:
								print ("ERROR:	  WRONG ASSIGNMENT FOR BOOLEAN VARIABLE")
						elif value[1] == 'STR' and target in self.str:
							self.str[target] = s[1]
							self.vars[target] = s[1]
							self.iter_var[target] = s[1]
						elif value[1] == 'NUM' and target in self.int:
							self.int[target] = s[1]
							self.vars[target] = s[1]
							self.iter_var[target] = s[1]
						else:
							print("ERROR:	VARIABLE ERROR, PAY ATTENTION TO %s" % instr[1][0])
							raise RuntimeError

					elif value[0] == 'BINOP':
						value = instr[2]
						a = self.eval(value)
						s.append(a[1])
						s.append(a[0])
						if s[1] == 'NUM':
							self.int[instr[1][0]] = s
						elif s[1] == 'BOOL':
							self.bool[instr[1][0]] = s
						elif s[1] == 'STR':
							self.str[instr[1][0]] = s
						self.vars[instr[1][0]] = s
						self.iter_var[instr[1][0]] = s

					elif value[1] == 'LNS':
						s.append(self.lms_var)
						s.append('NUM')
						self.int[target] = s
						self.vars[target] = s
						self.iter_var[target] = s
				else:
					print ("ERROR:	VARIABLE NOT INITIALIZED %s" % instr[1][0])
					raise RuntimeError


			elif op == 'IF':
				loopvar = instr[1]
				initval = instr[2]
				if self.releval(loopvar) == True:
					if loopvar[2][1][0] == 'NUM':
						var1 = loopvar[2][0][0]
						if var1 in self.int:
							self.rec(initval)
					elif loopvar[2][0][0] == 'BOOL' or loopvar[2][1][0] == 'BOOL':
						var1 = loopvar[2][0][0]
						if var1 in self.bool:
							self.rec(initval)
					elif loopvar[2][0][0] == 'STR' and loopvar[2][1][0] == 'STR':
						var1 = loopvar[2][0][0]
						if var1 in self.str:
							self.rec(initval)
						else:
							print("ERROR:	UNDEFINED VARIABLE ")
							raise RuntimeError
					else:
						print ("ERROR:    UNDEFINED VARIABLE ")
						raise RuntimeError
				else:
					print ("ERROR:    CANNOT SOLVE FOR IF-ELSE")
					raise RuntimeError


			elif op == 'VECTOR':
				x = 7
				for vname in instr[2]:
					self.lists[vname] = [0] * x


			elif op == 'INDEX_AS':
				target = instr[1][0]
				value = []
				if target in self.lists:
					place = int(instr[2])
					value.append('INDEX')
					value.append(target)
					value.append(instr[3])
					self.lists[target][place] = instr[3]
				else:
					print("ERROR:	UNDEFINED VARIABLE %s" % instr[1][0])
					raise RuntimeError


			elif op == 'VECTOPER':
				pass


			elif op == 'IF-LOTS':
				loopvar = instr[1]
				initval = instr[2]
				if self.releval(loopvar) == True:
					if loopvar[2][1][0] == 'NUM' or loopvar[2][0][0] == 'NUM':
						var1 = loopvar[2][0][0]
						if var1 in self.int:
							#print ('Here&'), initval
							self.rec(initval)
					elif loopvar[2][0][0] == 'BOOL' or loopvar[2][1][0] == 'BOOL':
						var1 = loopvar[2][0][0]
						if var1 in self.bool:
							self.rec(initval)
					elif loopvar[2][0][0] == 'STR' or loopvar[2][1][0] == 'STR':
						var1 = loopvar[2][0][0]
						if var1 in self.str:
							self.rec(initval)
						else:
							print("ERROR:	UNDEFINED VARIABLE ")
							raise RuntimeError
					else:
						print ("ERROR:    UNDEFINED VARIABLE ")
						raise RuntimeError
				else:
					print ("ERROR:    CANNOT SOLVE FOR IF-ELSE")
					raise RuntimeError


			elif op == 'DO-UNTIL':
				ok = True
				loopvar = instr[2]
				initval = instr[1]
				self.rec(initval)
				while (ok):
					if self.releval(loopvar) == True:
						self.rec(initval)
					else:
						ok = False

			# FUNCTION STATEMENT


			elif op == 'PROCEDURE':
				self.save_args = instr[2]
				self.kol_args = len(instr[2])
				if instr[1] in self.func:  
					self.rec(self.func[instr[1]])
				else:
					print("ERROR:	FUNCTION NOT DESCRIBED")
					raise RuntimeError


			elif op == 'PROCEDURE_NUMS':
				i = len(instr[2])
				for el in instr[2]:
					if type(el) != int:
						print ("ERROR:   CHECK TYPES IN FUNCTION ARGUMENTS")
				self.kol_args = len(instr[2])
				if (self.kol_args < self.kol_args_in_func):
					print ('ERROR:	 TOO LITTLE OF ARGUMENTS')
					raise RuntimeError
				s = []
				s = instr[2]
				self.save_args = s
				self.assign_default(instr[2])  				# put into self.func_args_iter
				self.kol_args_in_func_iter = self.kol_args_in_func
				if instr[1] in self.func:
					self.rec(self.func[instr[1]])
				else:
					print("ERROR:	FUCNTION NOT DESCRIBED")
					raise RuntimeError

			elif op == 'PROC_NO_ARG':
				if instr[1] in self.func:
					if self.kol_args_in_func == 0:
						self.rec(self.func[instr[1]])
				print 'ERROR:   PROCEDURE WITH NO ARGUMENT'

			elif op == 'FUNCTION':
				self.kol_args_in_func = 0
				self.sev_args = 0
				self.kol_args_in_func_iter = 0
				i = 1
				retval = []
				actions = []
				for el in instr[3]:
					self.kol_args_in_func += 1
					self.kol_args_in_func_iter += 1
					self.func_args.append(el)
					self.func_args_iter.append(list(el))
					i = i + 1
					if el == '...':
						self.sev_args = 1
						self.kol_args_in_func -= 1
						self.kol_args_in_func_iter -= 1
						self.func_args_iter = self.func_args_iter[:-1]
				for el in instr[4]:
					actions.append(el)
				self.func[instr[2]] = actions
				retval.append(instr[1])
				retval.append(instr[5])
				self.func_ret[instr[2]] = value
				if instr[5][0] not in instr[3]:
					print "ERROR:	THE VARIABLE IS NOT FOUND IN THE LIST OF ARGUMENTS"
					raise RuntimeError
				

				

			# ROBOT STATEMENT

			elif op == 'ROBOT':
				self.create_robot(instr[1], instr[2])
				print("\nROBOT CREATED\n")
				self.print_cell()


			elif op == 'FORWARD':
				self.forward()
				self.print_cell()
				if self.check_finish_in_lab() == 1:
					self.found = 1
					break

			elif op == 'BACK':
				self.back()
				self.print_cell()
				if self.check_finish_in_lab() == 1:
					self.found = 1
					break

			elif op == 'LEFT':
				self.left()
				self.print_cell()
				if self.check_finish_in_lab() == 1:
					self.found = 1
					break

			elif op == 'RIGHT':
				self.right()
				self.print_cell()
				if self.check_finish_in_lab() == 1:
					self.found = 1
					break

			elif op == 'ROTATE_LEFT':
				self.rotate_left()

			elif op == 'ROTATE_RIGHT':
				self.rotate_right()

			elif op == 'LMS':
				print 'LMS ACTIVATED'
				self.lms()

			elif op == 'REFLECT':
				print 'REFLECTOR ACTIVATED'
				self.reflect()

			elif op == 'DRILL':
				print 'DRILL ACTIVATED'
				self.drill()
				self.print_cell()
				if self.check_finish_in_lab() == 1:
					self.found = 1
					break

			elif op == 'RETURN':
				print("ERROR:	BIG ERROR")
				raise RuntimeError

			elif op == 'LMS_':
				self.lms()

			self.pc += 1
			if self.found == 1:
				break;


####################################################################################


	def rec(self, instr):
		k = 0
		spisok = instr
		n = len(spisok)
		while k < n:
			instr = spisok[k]
			k = k + 1
			fp = instr[0]

			if fp == 'PRINT':
				plist = instr[1]
				out = ""
				if plist[0] in self.iter_var:
					for value in plist:
						evaling = self.vars[value]
						print evaling[0]
				elif plist[0] in self.vars:
					for value in plist:
						evaling = self.vars[value]
						print evaling[0]
				elif plist[0] in self.lists:
					print "\t"
					for el in self.lists[plist[0]]:
						print el[1], 
					print '\n'
				else:
					print ('ERROR:	CANNOT FIND THIS VARIABLE')  



			# VARIABLE DECLARATION statement
			elif fp == 'INTEGER':
				target = instr[1]
				value = 0
				self.assign(target, value, op)
			elif fp == 'STRING':
				target = instr[1]
				value = ''
				self.assign(target, value, op)
			elif fp == 'BOOLEAN':
				target = instr[1]
				value = 'UNDEFINED'
				self.assign(target, value, op)

			
			# ASSIGN statement
			if fp == 'ASSIGN':
				target = instr[1][0]
				value = []
				value.append(instr[2][1])
				value.append(instr[2][0])
				s = []
				if target in self.vars:
					if (value[1] == 'BOOL' or value[1] == 'STR' or value[1] == 'NUM'):
						s.append(target)
						s.append(value)
						if value[1] == 'BOOL' and target in self.bool:
							if value[0] == 'true' or value[0] == 'false':
								self.bool[target] = s[1]
								self.vars[target] = s[1]
								self.iter_var[target] = s[1]
							else:
								print ("ERROR:	  WRONG ASSIGNMENT FOR BOOLEAN VARIABLE")
								raise RuntimeError
						elif value[1] == 'STR' and target in self.str:
							self.str[target] = s[1]
							self.vars[target] = s[1]
							self.iter_var[target] = s[1]
						elif value[1] == 'NUM' and target in self.int:
							self.int[target] = s[1]
							self.vars[target] = s[1]
							self.iter_var[target] = s[1]
						else:
							print("ERROR:	VARIABLE ERROR, PAY ATTENTION TO %s" % instr[1][0])
							raise RuntimeError
					elif value[1] == 'BINOP':				
						value = instr[2]
						self.save_procedure = value
						a = self.eval(value)
						s.append(a[1])
						s.append(a[0])
						if s[1] == 'NUM':
							self.int[instr[1][0]] = s
						elif s[1] == 'BOOL':
							self.bool[instr[1][0]] = s
						elif s[1] == 'STR':
							self.str[instr[1][0]] = s
						self.vars[instr[1][0]] = s
						self.iter_var[instr[1][0]] = s

						self.kol_args -= 1
						self.kol_args_in_func_iter -= 1

					elif value[1] == 'LNS':
						s.append(self.lms_var)
						s.append('NUM')
						self.int[target] = s
						self.vars[target] = s
				else:
					print ("ERROR:	VARIABLE NOT INITIALIZED %s" % instr[1][0])
					raise RuntimeError


			elif fp == 'INDEX_AS':
				target = instr[1][0]
				value = []
				if target in self.lists:
					place = int(instr[2])
					value.append('INDEX')
					value.append(target)
					value.append(instr[3])
					self.lists[target][place] = instr[3]
				else:
					print("ERROR:	UNDEFINED VARIABLE %s" % instr[1][0])
					raise RuntimeError

			elif fp == 'IF':
				loopvar = instr[1]
				initval = instr[2]
				if self.releval(loopvar) == True:
					if loopvar[2][1][0] == 'NUM':
						var1 = loopvar[2][0][0]
						if var1 in self.int:
							self.rec(initval)
					elif loopvar[2][0][0] == 'BOOL' or loopvar[2][1][0] == 'BOOL':
						var1 = loopvar[2][0][0]
						if var1 in self.bool:
							self.rec(initval)
					elif loopvar[2][0][0] == 'STR' and loopvar[2][1][0] == 'STR':
						var1 = loopvar[2][0][0]
						if var1 in self.str:
							self.rec(initval)
						else:
							print("ERROR:	UNDEFINED VARIABLE ")
							raise RuntimeError
					else:
						print ("ERROR:    UNDEFINED VARIABLE ")
						raise RuntimeError
				else:
					print ("ERROR:    CANNOT SOLVE FOR IF-ELSE")
					raise RuntimeError

			elif fp == 'IF-LOTS':
				loopvar = instr[1]
				initval = instr[2]
				if self.releval(loopvar) == True:
					if loopvar[2][1][0] == 'NUM':
						var1 = loopvar[2][0][0]
						if var1 in self.int:
							self.rec(initval)
					elif loopvar[2][0][0] == 'BOOL' or loopvar[2][1][0] == 'BOOL':
						var1 = loopvar[2][0][0]
						if var1 in self.bool:
							self.rec(initval)
					elif loopvar[2][0][0] == 'STR' and loopvar[2][1][0] == 'STR':
						var1 = loopvar[2][0][0]
						if var1 in self.str:
							self.rec(initval)
						else:
							print("ERROR:	UNDEFINED VARIABLE ")
							raise RuntimeError
					else:
						print ("ERROR:    UNDEFINED VARIABLE ")
						raise RuntimeError
				else:
					print (" ")
					

			elif fp == 'DO-UNTIL':   # not like in the run function
				loopvar = instr[2]
				initval = instr[1]
				self.rec(initval)
				while not self.releval(loopvar) == True:
					#print loopvar
					if loopvar[2][0] == 'VAR':
						var1 = loopvar[2][1][0]
						if var1 in self.vars:
							b = self.vars[var1][0]
							b = b + 1
							self.vars[var1][0] = b
							self.int[var1][0] = b
						else:
							print("UNDEFINED VARIABLE ")
							raise RuntimeError
					self.rec(initval)

			elif fp == 'VECTOPER':
				pass

			# FUNCTION STATEMENT

			elif fp == 'PROCEDURE':
				#print instr[1]
				if instr[1] in self.func:  
					self.rec(self.func[instr[1]])
				else:
					print("ERROR:	FUNCTION NOT DESCRIBED")
					raise RuntimeError

			elif fp == 'FUNCTION':
				actions = []
				actions.append(instr[4])
				self.func[instr[2]] = actions   

			# ROBOT STATEMENT

			elif fp == 'ROBOT':
				self.create_robot(instr[1], instr[2])
				print("ROBOT CREATED")
				self.print_cell()


			elif fp == 'FORWARD':
				self.forward()
				self.print_cell()
				if self.check_finish_in_lab() == 1:
					self.found = 1
					break

			elif fp == 'BACK':
				self.back()
				self.print_cell()
				if self.check_finish_in_lab() == 1:
					self.found = 1
					break

			elif fp == 'LEFT':
				self.left()
				self.print_cell()
				if self.check_finish_in_lab() == 1:
					self.found = 1
					break

			elif fp == 'RIGHT':
				self.right()
				self.print_cell()
				if self.check_finish_in_lab() == 1:
					self.found = 1
					break

			elif fp == 'ROTATE_LEFT':
				self.rotate_left()

			elif fp == 'ROTATE_RIGHT':
				self.rotate_right()

			elif fp == 'LMS':
				print 'LMS ACTIVATED'
				self.lms()

			elif fp == 'REFLECT':
				print 'REFLECTOR ACTIVATED'
				self.reflect()

			elif fp == 'DRILL':
				print 'DRILL ACTIVATED'
				self.drill()
				self.print_cell()
				if self.check_finish_in_lab() == 1:
					self.found = 1
					break;

			if self.kol_args > self.kol_args_in_func_iter and self.kol_args_in_func_iter == 1:
				if self.kol_args_in_func_iter == 1 and self.kol_args > 1:
					self.flag = 1
					k = len(self.rest_of_args)
					p = 0
					while p != k:
						var = self.rest_of_args[p]
						work = []
						my_procedure = []
						for el in self.save_procedure:
							my_procedure.append(el)
						my_procedure[3] = list(var)
						work = my_procedure
						if work[0] == 'BINOP':
							s = []
							a = self.eval(work)
							s.append(a[1])
							s.append(a[0])
							if s[1] == 'NUM':
								self.int[instr[1][0]] = s
							self.iter_var[instr[1][0]] = s
						self.kol_args = self.kol_args - 1
						p = p + 1
				print self.int[instr[1][0]][0]
				del self.rest_of_args[:]
				del self.save_args[:]
				for keys in self.iter_var.values():
					keys[0] = 0
					keys[1] = 'NUM'
				for keys in self.vars.values():
					keys[0] = 0

				 

			if self.found == 1:
				break;


###########################################################################################


   # Erase the current program
	def new(self):
		self.prog = {}

	# Insert statements
	def add_statements(self, prog):
		for line, stat in prog.items():
			self.prog[line] = stat

	# Delete a statement
	def del_line(self, lineno):
		try:
			del self.prog[lineno]
		except KeyError:
			pass
