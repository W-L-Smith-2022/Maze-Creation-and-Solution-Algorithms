# Maze-Creation-and-Solution-Algorithms
A project making and visualizing a couple of perfect maze creation algorithms and a couple of perfect maze solution algorithms. 
This project works with the Hunt and Kill perfect maze creation algorithm, the Growing Tree perfect maze creation algorithm, the Dead End Filler perfect maze solution algorithm, and the Shortest Path Finder perfect maze solution algorithm. <br />
Link to playlist of YouTube videos of visualizations of maze creation and solution algorithms: https://www.youtube.com/playlist?list=PLDQ-bcm9sjaUVhJ3mAJmWygHiuV5zggHo <br />
List and description of various maze creation and solution algorithms: https://www.astrolog.org/labyrnth/algrithm.htm <br />
List, description, and visualization of various maze creation and solution algorithms: https://www.jamisbuck.org/mazes/ <br/>
### What is a "Perfect" Maze?
In computer science, a "perfect" maze is one where there is one and only one path from any one cell to any other cell. <br />
A "perfect maze solution algorithm is one that solves "perfect" mazes. <br />
We will explore two "perfect" maze creation algorithms and solve the resulting mazes with two "perfect" maze solution algorithms. <br />
The demonstrations in this project do not represent the time it takes the algorithm to accomplish it's task. At this scale, most of these algorithms finish nearly instantaneously. <br />
The mazes are solved from the top left to the bottom right in this project. <br />
## Perfect Maze Creation Algorithms <br />
### Hunt and Kill:
#### How it Works:
* This algorithm starts like the Recursive Backtracker maze creation algorithm.
* It explores a randomly picked cell adjacent to the starting cell and sets the new cell as the current cell. 
* It then randomly picks a cell adjacent to the current cell, explores the new cell, sets the new cell as the current cell, and repeats this process until it dead ends into itself.
* When this happens, the program "Hunts" through the maze, looking for an explored cell adjacent to an unexplored cell.
* If it finds an acceptable cell, it sets this as the new current cell and repeats the process.
* If it scans the entire maze and does not finda an acceptable cell, that means that the maze has been created and the program ends.
#### Key for Hunt and Kill Visualizations:
* White Cells = Explored
* Gray Cells = Unexplored
* Black Cells = Walls
* Red Cells = Current Cell
* Blue Cells = Cells Being Tested for Unexplored Neighbors
### Growing Tree:
#### How it Works:
* A starting cell is added to a list and is set as the current cell. And unexplored neighbor of the current cell is randomly chosen, explored, and added to the list.
* A cell is then chosen from the list and is set as the current cell.
* If the current cell has no unexplored neighbors, it is removed from the list.
* If the current cell has any unexplored neighbors, one of them is randomly chosen, explored, and is added to the list.
* This is repeated until there is nothing left in the list.
#### How to Choose the Current Cell:
* The interesting part is how you choose what cell from the list is set to be your current cell.
* If you choose the last (or most recent) cell on the list, the algorithm mimics (or effectively becomes) the Recursive Backtracker Algorithm.
* If you randomly choose a cell from the list, the algorithm produces similar results to prim's algorithm.
* If you always choose the first cell on the list, the maze becomes very "blocky."
* You can combine various ways of selecting your current cell to get some interesting textures.
* In this project's Growing Tree demonstrations, the mazes were created where the first cell on the list was chosen 65% of the time and a randomly chosen cell from the list was chosen 35% of the time.
#### Key for Growing Tree Visualizations:
* White = Explored
* Gray = Unexplored
* Black = Wall
* Red = Current Cell
* Blue = Cell Being Added to List
## Perfect Maze Solution Algorithms <br />
### Dead End Filling:
#### How it Works:
* The algorithm systematically scans through the array looking for any cell that hass only one non fillled neighbor (aka dead end).
* It fills the discovered dead end unless it is the start or end.
* It repeats these steps until there are no more dead ends left.
* This results in a path of unfilled cells from the start to the end.
#### Key for Dead End Filling Visualizations:
* White = Unexplored Cell
* Black = Wall
* Gray = Filled in Cell
* Blue = Cell Being Filled In
* Red = Path
### Shortest Path Finder:
#### How it Works:
* The starting cell is filled with "water."
* The cells filled with "water" fill all unfilled adjacent cells with "water," and the cells record what cell they were filled by.
* This is repeated until either the maze is filled with "water," or until the end is filled.
* The path is then traced from the end back to the start by following which cell filled which from the end to the start.
#### Key for Dead End Filling Visualizations:
* White = Unfilled Cell
* Black = Wall
* Blue = Cells Filled with "Water"
* Yellow = Cells Being Filled
* Red = Path
# Information About Other Projects <br />
Link to YouTube Channel: https://www.youtube.com/channel/UCOnHMcTYB7Po4chwtugLfyw <br />
Link to my GitHub: https://github.com/W-L-Smith-2022
## 2D-Turtle-With-Unity <br />
This project is about creating a Two Dimensional Version of the Turtle Program (or Turtle Graphics) using Unity. <br />
Playlist of YouTube Videos in this Sereies: https://youtube.com/playlist?list=PLDQ-bcm9sjaU8BaX41JHdLagBaXN5XCiS <br />
Link to Unity Documentation: https://docs.unity3d.com/Manual/index.html <br />
### 2D-Turtle-With-Unity-Part-1
This project is about getting started with Unity and using scripts to make objects move in Unity. <br />
Link to YouTube video about this project: https://youtu.be/AWbCPk5Z3FQ <br />
Link to Unity Documentation: https://docs.unity3d.com/Manual/index.html <br />
Link to GitHub for this Project: https://github.com/W-L-Smith-2022/2D-Turtle-With-Unity-Part-1 <br />
<br />
### 2D-Turtle-With-Unity-Part-2
This project is about using C# Scripts to move around in the game view in Unity. <br />
Link to YouTube video about this project: https://youtu.be/buvePt4hVHI <br />
Link to Unity Documentation: https://docs.unity3d.com/Manual/index.html <br />
Link to GitHub for this Project: https://github.com/W-L-Smith-2022/2D-Turtle-With-Unity-Part-2 <br />
<br />
### 2D-Turtle-With-Unity-Part-3
This project is about using the mouse wheel to zoom in/out in the game view in Unity. <br />
Link to YouTube video about this project: https://youtu.be/mWD0ehrNvJk <br />
Link to Unity Documentation: https://docs.unity3d.com/Manual/index.html <br />
Link to GitHub for this Project: https://github.com/W-L-Smith-2022/2D-Turtle-With-Unity-Part-3 <br />
<br />
