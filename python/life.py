
import doctest
import copy

def test():
	"""
	>>> test()
	42
	"""
	return 42


def strToWorld(s):
	rows = s.split(',')
	world = []
	for r in rows:
		arr = []
		for c in r:
			if c.isdigit():
				arr.append(int(c))
			else:
				arr.append(c)
		world.append(arr)
	return world


def countNeighbours(world, row, col):
	sum = 0
	countRows = len(world)
	countCols = len(world[0])
	for iRow in range(-1,2):
		for iCol in range(-1,2):
			if not (iRow == 0 and iCol == 0):
				idxRow = (row + iRow) % countRows
				idxCol = (col + iCol) % countCols
				sum = sum + world[idxRow][idxCol] 
	return sum 



def calcNewWorld(world, logic):
	newWorld = copy.deepcopy(world)
	countRows = len(world)
	countCols = len(world[0])
	for iRow in range(countRows):
		for iCol in range(countCols):
#			print iRow, iCol
			nNeighbours = countNeighbours(world, iRow, iCol)
			me = world[iRow][iCol] % 2
			newValue = logic[nNeighbours][me]
			newWorld[iRow][iCol] = newValue
	return newWorld

def outputWorld(world):
	for r in world:
		s = ""
		for c in r:
			if c == 1:
				s = s+'*'
			else:
				s = s+'.'
#			s = s + str(c)
		print s


a = [ [1,0,0,4,5], [6,7,8,9,10] ]
stringWorld = \
"000000000," \
"000001000," \
"000011000," \
"000001000," \
"000000000," \
"000000000"

logic = { 0:[0,0],1:[0,0],2:[0,1],3:[1,1], 4:[0,0], 5:[0,0], 6:[0,0], 7:[0,0], 8:[0,0] }


#print field

world = strToWorld(stringWorld)

for i in range(10):
	outputWorld(world)
	world = calcNewWorld(world, logic)
	print "---"

if __name__ == "__main__": 
    doctest.testmod()
