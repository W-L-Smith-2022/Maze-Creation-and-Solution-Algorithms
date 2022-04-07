#DFS: DEPTH FIRST SEARCH		Recursive Backtracking, RBT
#BFS: BREADTH FIRST SEARCH		Prim Algorithm,			Shortest Path Algorithm/Dijkstras


import numpy as np
import  cv2
import random



NEW = 50
FILLED = 100
PATH = 200
I=0
#Always solve from upper left to bottom right

def show(img, scale=8, wait=0):
	h,w=img.shape
	out=np.zeros((h,w,3),dtype=np.uint8)
	#this is in BGR, not RGB
	out[img==255]=(255,255,255)
	out[img==100]=(255,0,0)
	out[img==50]=(0,255,255)
	out[img==200]=(0,0,255)
	out=cv2.resize(out,(w*scale,h*scale), None, interpolation=cv2.INTER_NEAREST)
	cv2.imshow("test",out)
	cv2.waitKey(wait)

# def save(img):
	# h,w=img.shape
	# out=np.zeros((h,w,3),dtype=np.uint8)
	# out[img==255]=(255,255,255)
	# out[img==100]=(255,0,0)
	# out[img==50]=(0,255,255)
	# out[img==200]=(0,0,255)
	# global I
	# #cv2.imwrite(f"{I:05d}.png",out)
	# I=I+1
	# print(I)

maze=cv2.imread("growingTreeMaze.png",0)
start = (1,1)
h,w=maze.shape
end=(h-2,w-2)

def findPath(maze, stack, current):
	for i in stack:
		filledBy, cell = i
		if cell==current:
			maze[current]=PATH
			temp = filledBy*1
			stack.remove(i)
			return temp

def getNeighbors(maze, current):
	y,x=current
	h,w=maze.shape
	neighbors=[]
	for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
		yp=y+dy
		xp=x+dx
		if h>yp>0<xp<w and maze[yp,xp]==255:
			neighbors.append((yp,xp))
	return neighbors

stack = [(start, start)]
beginning = stack[0]*1
maze[start]=FILLED
for i in stack:
	filledBy, current = i
	neighbors = getNeighbors(maze, current)
	maze[current]=FILLED
	for neighbor in neighbors:
		stack.append((current, neighbor))
		maze[neighbor]=NEW
	#show(maze,wait=10)
	save(maze)
current = end
while beginning in stack:
	current = findPath(maze, stack, current)
	#show(maze, wait=10)
	save(maze)


#show(maze)
save(maze)
