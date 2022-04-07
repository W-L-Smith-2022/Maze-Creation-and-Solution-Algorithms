#DFS: DEPTH FIRST SEARCH		Recursive Backtracking, RBT
#BFS: BREADTH FIRST SEARCH		Prim Algorithm,			Shortest Path Algorithm/Dijkstras
#This Program Creates a Maze Via a Hunt and Kill Algorithm
#h<=70
#1080x1920

import numpy as np
import  cv2
import random

w=32
h=18
UNEXPLORED=200
WALL=0
EXPLORED=255
HUNT=130
CURRENT = 100
I=0
#Always solve from upper left to bottom right

# def ogShow(img, scale=8, wait=0):
	# h,w=img.shape
	# out=cv2.resize(img,(w*scale,h*scale), None, interpolation=cv2.INTER_NEAREST)
	# #f = open("cv2file.txt", "w")
	# #f.write(out)
	# #f.close()
	# cv2.imshow("test",out)
	# #if wait!=0:
	# #	wait+=20
	# cv2.waitKey(wait)
#def show(img, scale=20, wait=0):
def save(img):#actually show function, just changed names to avoid accidentally saving stuff
	scale=20
	wait =1
	h,w=img.shape
	out=np.zeros((h,w,3),dtype=np.uint8)
	#this is in BGR, not RGB
	out[img==255]=(255,255,255)
	out[img==200]=(200,200,200)
	out[img==100]=(0,0,255)
	out[img==130]=(255,0,0)
	out=cv2.resize(out,(w*scale,h*scale), None, interpolation=cv2.INTER_NEAREST)
	cv2.imshow("test",out)
	cv2.waitKey(wait)

# def save(img):
	# h,w=img.shape
	# out=np.zeros((h,w,3),dtype=np.uint8)
	# out[img==255]=(255,255,255)
	# out[img==200]=(200,200,200)
	# out[img==100]=(0,0,255)
	# out[img==130]=(255,0,0)
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

def hunt(maze):
	for y in range(1, h*2, 2):
		for x in range(1, w*2, 2):
			temp=maze[y,x]*1
			maze[y,x]=HUNT
			#show(maze, wait=1)
			save(maze)
			maze[y,x]=temp
			if getUnexploredNeighbors(maze,(y,x)):
				return y,x
	return []

def knockDownWall(maze,a,b):
	y1,x1=a
	y2,x2=b
	x=(x1+x2)//2
	y=(y1+y2)//2
	maze[y,x]=EXPLORED
	

maze=np.zeros((h*2+1,w*2+1),dtype=np.uint8)
maze[1::2,1::2]=UNEXPLORED

maze[1,1]=EXPLORED


current = (1,1)
while current:
	maze[current]=CURRENT
	#show(maze,wait=1)
	save(maze)
	neighbors=getUnexploredNeighbors(maze, current)
	if neighbors:
		neighbor=random.choice(neighbors)
		yn,xn=neighbor
		maze[yn,xn]=EXPLORED
		knockDownWall(maze,current,neighbor)
		maze[current]=EXPLORED
		current = neighbor
	else:
		#HUNTING=True
		maze[current]=EXPLORED
		current = hunt(maze)
	#show(maze, wait=1)
	save(maze)
#show(maze)
save(maze)
#print("Show Done")


#cv2.imwrite("huntAndKill.png",maze)
print("Saved")
