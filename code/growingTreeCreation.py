#DFS: DEPTH FIRST SEARCH		Recursive Backtracking, RBT
#BFS: BREADTH FIRST SEARCH		Prim Algorithm,			Shortest Path Algorithm/Dijkstras


import numpy as np
import  cv2
import random

w=32
h=14
UNEXPLORED=200
WALL=0
EXPLORED=255
CURRENT=100
NEIGHBOR=50
I=0
#Always solve from upper left to bottom right

def show(img, scale=8, wait=0):
	h,w=img.shape
	out=np.zeros((h,w,3),dtype=np.uint8)
	#this is in BGR, not RGB
	out[img==255]=(255,255,255)
	out[img==200]=(200,200,200)
	out[img==100]=(0,0,255)
	out[img==50]=(255,0,0)
	out=cv2.resize(out,(w*scale,h*scale), None, interpolation=cv2.INTER_NEAREST)
	cv2.imshow("test",out)
	cv2.waitKey(wait)
	
# def save(img):
	# h,w=img.shape
	# out=np.zeros((h,w,3),dtype=np.uint8)
	# out[img==255]=(255,255,255)
	# out[img==200]=(200,200,200)
	# out[img==100]=(0,0,255)
	# out[img==50]=(255,0,0)
	# global I
	# #cv2.imwrite(f"{I:05d}.png",out)
	# I=I+1
	# print(I)

def getUnexploredNeighbors(maze, current):
	y,x=current
	h,w=maze.shape
	neighbors=[]
	for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
		yp=y+2*dy
		xp=x+2*dx
		if h>yp>0<xp<w and maze[yp,xp]==UNEXPLORED:
			neighbors.append((yp,xp))
	return neighbors

def knockDownWall(maze,a,b):
	y1,x1=a
	y2,x2=b
	x=(x1+x2)//2
	y=(y1+y2)//2
	# //does int division
	maze[y,x]=EXPLORED
	

maze=np.zeros((h*2+1,w*2+1),dtype=np.uint8)
maze[1::2,1::2]=UNEXPLORED

maze[1,1]=EXPLORED

stack = [(1,1)]
while stack:
	rand = random.random()
	#if rand<.66:
	#	current=stack[0]
	#else:
	#	current=random.choice(stack)
	current=stack[0]
	maze[current] = CURRENT
	#show(maze, wait=1)
	#save(maze)
	#current = stack[0]
	neighbors=getUnexploredNeighbors(maze, current)
	if neighbors:
		neighbor = random.choice(neighbors)
		yn,xn=neighbor
		maze[yn,xn]=NEIGHBOR
		knockDownWall(maze, current, neighbor)
		#show(maze, wait=1)
		#save(maze)
		maze[yn,xn]=EXPLORED
		stack.append(neighbor)
	else:
		stack.remove(current)
	maze[current]=EXPLORED
	h,w=maze.shape
	#show(maze, wait=1)
#stack=[(1,1)]
# while stack:
	# current=random.choice(stack)
	# # if random.random()<.75:
		# # current=stack[-1]
	# #current=stack[-1]
	# #current=random.choice(stack)
	# #current=stack[0]
	# neighbors=getUnexploredNeighbors(maze, current)
	# if neighbors:
		# neighbor=random.choice(neighbors)
		# #neighbor=neighbors[0]
		# yn,xn=neighbor
		# maze[yn,xn]=EXPLORED
		# knockDownWall(maze,current,neighbor)
		# stack.append(neighbor)
	# else:
		# stack.remove(current)
	# h,w=maze.shape
	# show(maze, wait=1)
#show(maze)
#save(maze)
print('done')


# def makeMaze(maze, loc):
	# y,x=loc
	# maze[y,x]=EXPLORED
	# while neighbors:=getUnexploredNeighbors(maze, loc):#:=stores and gives results of what just got stored
		# neighbor=random.choice(neighbors)
		# knockDownWall(maze,loc,neighbor)
		# makeMaze(maze,neighbor)

# makeMaze(maze, (1,1))

cv2.imwrite("blockyGrowingTreeMaze.png",maze)
