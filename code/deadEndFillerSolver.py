#DFS: DEPTH FIRST SEARCH		Recursive Backtracking, RBT
#BFS: BREADTH FIRST SEARCH		Prim Algorithm,			Shortest Path Algorithm/Dijkstras


import numpy as np
import  cv2
import random


# EXPLORED=254
# WALL=0
# UNEXPLORED=255
FILLED = 100
PATH = 200
CURRENT = 50
I=0
#Always solve from upper left to bottom right

def show(img, scale=8, wait=0):
	h,w=img.shape
	out=np.zeros((h,w,3),dtype=np.uint8)
	#this is in BGR, not RGB
	out[img==255]=(255,255,255)
	out[img==100]=(100,100,100)
	out[img==50]=(255,0,0)
	out[img==200]=(0,0,255)
	out=cv2.resize(out,(w*scale,h*scale), None, interpolation=cv2.INTER_NEAREST)
	cv2.imshow("test",out)
	cv2.waitKey(wait)
	
# def save(img):
	# h,w=img.shape
	# out=np.zeros((h,w,3),dtype=np.uint8)
	# out[img==255]=(255,255,255)
	# out[img==100]=(100,100,100)
	# out[img==50]=(255,0,0)
	# out[img==200]=(0,0,255)
	# global I
	# #cv2.imwrite(f"{I:05d}.png",out)
	# I=I+1
	# print(I)

maze=cv2.imread("growingTreeMaze.png",0)
start = (1,1)
h,w=maze.shape
end=(h-2,w-2)

def getNeighbors(maze, current):
	y,x=current
	h,w=maze.shape
	neighbors=[]
	for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
		yp=y+dy
		xp=x+dx
		if h>yp>0<xp<w and maze[yp,xp]==255 and maze[y,x]==255 and (y,x)!=start and (y,x)!=end:
			neighbors.append((yp,xp))
			#maze[yp,xp]=100
	return neighbors

def findDeadEnds(maze):
	h,w=maze.shape
	for y in range(1, h*2):
		for x in range(1, w*2):
			if len(getNeighbors(maze,(y,x)))==1:
				maze[y,x]= CURRENT
				#show(maze, wait=1)
				save(maze)
				return y,x
	return []

def findPath(maze, stack):
	y,x=stack[-1]
	h,w=maze.shape
	for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
		yp=y+dy
		xp=x+dx
		if h>yp>0<xp<w and maze[yp,xp]==255:
			return (yp,xp)

deadEndsExist = True
#i=0
while deadEndsExist:
	current = findDeadEnds(maze)
	if current:
		maze[current]=FILLED
	else:
		deadEndsExist=False
	#print(i)
	#i+=1
	#show(maze,wait=1)
	save(maze)

stack = [start]
while end not in stack:
	maze[stack[-1]]=PATH
	stack.append(findPath(maze,stack))
maze[end]=PATH

#show(maze)
save(maze)
