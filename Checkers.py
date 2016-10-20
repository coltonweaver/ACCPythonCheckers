def checkLegal():

def doubleMove():

def kingMe():

#Priority
def playerMovement():

#Priority
def checkWin():

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
