''' 
 life
'''


import time
import os
import random

WIDTH = 60
HEIGHT = 40
ON = "o"
OFF = " "

def createRow():
	row = ""
	for i in range(WIDTH):
		if random.randint(1,8) == 1:
			row += ON
		else:
			row += OFF
	return row

def createWorld():
	w = []
	for i in range(HEIGHT):
		row = createRow()
		w.append( row )
	return w


def outputWorld(w):
	for i in range(len(w)):
		print w[i]


def calcNeighbours(w, ir, ic):
	'''
	>>> w = [ 
	...		('..o.'), 
	...		('oooo'), 
	...		('ooo.') 
	...		]
	>>> w[0][3]
	'.'
	>>> w[2][3]
	'.'
	>>> calcNeighbours(w, 0, 0)
	2
	>>> calcNeighbours(w, 0, 1)
	4
	>>> calcNeighbours(w, 0, 2)
	3
	>>> calcNeighbours(w, 0, 3)
	3
	>>> calcNeighbours(w, 1, 1)
	6
	'''
	cnt = 0
	maxR = len(w)
	maxC = len(w[0])
	for r in range(-1,2):
		for c in range(-1,2):
			idx_r = ir+r
			idx_c = ic+c
			calc = True
			if (ir == idx_r  and  ic==idx_c):
				calc = False
			elif (idx_r < 0  or  idx_r >= maxR):
				calc = False
			elif (idx_c < 0  or  idx_c >= maxC):
				calc = False
			if calc:
#				print "r:", idx_r, " c:", idx_c
				if w[idx_r][idx_c] == ON:
					cnt = cnt+1
	return cnt


def calcNewWorld(ow):
	newWorld = []
	for ir in range(len(ow)):
		row = ow[ir]
		newRow = ""
		for ic in range(len(row)):

			cnt = calcNeighbours(ow, ir, ic)
			me = ow[ir][ic]
			if me == OFF  and  cnt == 3:
				newCell = ON
			elif me == ON  and  (cnt == 2 or cnt == 3):
				newCell = ON
			else:
				newCell = OFF
#			newCell = str(cnt)
			newRow = newRow + newCell
		newWorld.append(newRow)
	return newWorld


def main():
	world = createWorld()
	generation = 500
	while generation > 0:
		os.system('clear')
		outputWorld(world)
		time.sleep(0.5)
		world = calcNewWorld(world)
		generation = generation-1


main()

w = [ 
	('..*.'), 
	('.*.*'), 
	('***.') 
	]
#calcNeighbours(w, 0, 3)



if "__main__" == __name__:
	import doctest
	doctest.testmod()

