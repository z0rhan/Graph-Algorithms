Here are the instructions and things to be careful of:
1. First of all, the code was designed to read files where the data are given in the format of those ten public cases.
The code is going to exit if the format does not match.
The format are;
1: 2 3 4 5 ... for edges
1 2 5 7 8 ... for the set of vertices
1 100 for the pair

---------------------------------------------------------IMPORTANT---------------------------------------------------------------------------
I'm adding this here because for the three test cases it says a single vertex belonging or not belonging to set, 
so please write the pair as "1 1" as it means from 1 to 1 here.
->"1 1" if you want to find a path from 1 to 1

Also, I have not handled the code to add a vertex with wihtout edges as the edges are stored in a dictionary.

For the set, if you want a empty set, then just leave the file name empty. 

I'm sorry for all this but I had very little time to take care of small details like this. 
Eventually, I'll take care of this and update them on my github but I can't finish them before the deadline
---------------------------------------------------------------------------------------------------------------------------------------------

The package provided will likely be a zip file. You can unzip it and it will have following files:
1. bfs-maximal-vertices.py
2. graph.py
3. README.txt
4. All 10 public test cases

 The graph.py file contains the graph class that I implemented myself. You can skip this file.

 The algorithm is placed in the maxvertices.py file. I have comments explaining the code at least for the algorithm.

 You can open the terminal in the directory where these file are located and execute the code with 
 either "python3 bfs-maximal-vertices.py" or "python bfs-maximal-vertices.py"

 But before this make sure the file containing the test cases are in the same directory too.

 You'll be asked to input the file name containing the edges, set and the pair of vertices.
 And, the maximal vertices the belong to the set occuring in the shortest path is printed in the screen.

