
def checkLegal(checkerboard[x][y],checkerboard[x1][y1]):
	#Please someone rewrite this so it works!
	def isAt():
		if checkerboard[x][y] == "x"
			return True
		else 
			return False

	def pieceBlock():
		for num in range(x1,x)
			for num1 in range (y1,y)
				if checkerboard[num][num1] is full
					return False
				else
					return True

	def sameTeam():
		if playerCall.piece() is pieceBlock()
			return True
		else 
			return False

	def diffTeam():
		if playerCall.piece() is not pieceBlock();
			retrun True
		else 	
			return False

	if playerCall.isAt(x,y) is True:
		if player.checkerboard[x1][y1] is None
			return False
		else if playerCall.pieceBlock() is sameTeam()
			return False
		else if playerCall.pieceBlock() is diffTeam()
			#Sees if the space diagonal from the blocking piece is open
			#if it is then return True else return False
		else if playerCall.pieceBlock() is None
			if (piece != king)
				if (x1 == x):
					return False
				else if(y1 == y):
					return False
				else if (abs(x2 - x)> 1) or (abs(y2 -y) > 1)
					return False
				else
					return True
			else
				if(abs(x2-x)>1) or (abs(y2-y)>1)
					return False
				else 
					return True
	else
		return False

def doubleMove():

def kingMe():

#Priority
def playerMovement():

#Priority
white_peices=0		#these variables should be declared elsewhere in the program
black_peices=2		#and are purely for debuging purposes
def checkWin():
	#print "hello world"
	if(white_peices<1 or black_peices<1):	#because there cannot be a tie, the if statement only checks for victory
		if(white_peices<black_peices):		#this will check which one of the variables has no peices left
			return 1						#if the white pieces win then a 2 will be returned
		else:								#and if black pieces win then a 1 will be retunred
			return 2
	else: return							#otherwise the funcdtion will terminate


#print checkWin()


#Priority
def rotateBoard():

def removePiece():

def initBoard():
	checkerboard = [['*']*9 for unused in range(9)]

	#This is just assigning the outer values
	checkerboard[0][0:8]="~","A","B","C","D","E","F","G","H"
	checkerboard[1][0]="1"
	checkerboard[2][0]="2"
	checkerboard[3][0]="3"
	checkerboard[4][0]="4"
	checkerboard[5][0]="5"
	checkerboard[6][0]="6"
	checkerboard[7][0]="7"
	checkerboard[8][0]="8"
	#checkerboard[1:8][0]="1","2","3","4","5","6","7","8"

	# checks for a pound sign above and next to it, forming a checker pattern
	for x in range (1,9):
		for y in range (1,9):
			if checkerboard[x][y-1]=="#":
				continue
			if checkerboard[x-1][y]=="#":
				continue
			checkerboard[x][y]="#"
			
	# lays out all of the pieces
	for x in range(1,4):
		for y in range(1,9):
			if checkerboard[x][y]=="#":
				continue
			checkerboard[x][y]="b"

	for x in range (6,9):
		for y in range(1,9):
			if checkerboard[x][y]=="#":
				continue
			checkerboard[x][y]="w"

def printBoard()
	# prints out the checkerboard with pieces
	for x in range (0,9):
		print (" | ".join(checkerboard[x][0:9]))
		#print checkerboard[x][0:9]

def main():
	initBoard()
	printBoard()
