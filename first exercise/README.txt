Here are the instructions and things to be careful of:

First of all, the code was designed to read files where the data are given in the format of those ten public cases.
The code is going to exit(Print the specific error if I manage to complete them) if the format does not match.

The format are;
1: 2 3 4 5 ... for edges
1 2 5 7 8 ... for the set of vertices
1 100 for the pair

---------------------------------------------------------IMPORTANT---------------------------------------------------------------------------
->"1 1" if you want to find a path from 1 to 1

->the code assumes that every vertex has outdegree at least 1. This has to do something with the graph being stored in a dictionary. 
I need to initialize the vertex with an empty list if it has no outdegree (Not the point of this exercise).

->For the set, if you want a empty set, then just leave the file name empty. 

I'll try to fix for the second point if I get some time.
---------------------------------------------------------------------------------------------------------------------------------------------

The package provided will likely be a zip file. You can unzip it and it will have following files:
1. bfs-maximal-vertices.py
2. graph.py
3. All 10 public test cases
The above files will be in a separate folder(bfs-maximal).

4. README.txt (This file)

 The graph.py file contains the graph class that I implemented myself(That's why it still needs some polishing). You can skip this file.

 The algorithm is placed in the bfs-maximal-vertices.py file. I have comments explaining the code at least for the algorithm.

 You can open the terminal in the directory where these file are located and execute the code with 
 either "python3 bfs-maximal-vertices.py" or "python bfs-maximal-vertices.py"

 But before this make sure the file containing the test cases are in the same directory too. (I did this for your convenience)

 You'll be asked to input the file name containing the edges, set and the pair of vertices.
 And, the maximal vertices the belong to the set occuring in the shortest path is printed in the screen.

