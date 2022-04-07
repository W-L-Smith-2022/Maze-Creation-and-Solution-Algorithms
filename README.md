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
### Hunt and Kill
How it Works:
* This algorithm starts like the Recursive Backtracker maze creation algorithm.
* It explores a randomly picked cell adjacent to the starting cell and sets the new cell as the current cell. 
* It then randomly picks a cell adjacent to the current cell, explores the new cell, sets the new cell as the current cell, and repeats this process until it dead ends into itself.
* When this happens, the program "Hunts" through the maze, looking for an explored cell adjacent to an unexplored cell.
* If it finds an acceptable cell, it sets this as the new current cell and repeats the process.
* If it scans the entire maze and does not finda an acceptable cell, that means that the maze has been created and the program ends.
<br />
Key for Hunt and Kill Visualizations:
* White Cells = Explored
* Gray Cells = Unexplored
* Black Cells = Walls
* Red Cells = Current Cell
* Blue Cells = Cells Being Tested for Unexplored Neighbors
<br />
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
