Project 2: Topic-Specific PageRank 

This project implements Topic-Specific PageRank algorithm using Python. Please download the zipped folder 
and run the tspr.py file using Python IDE or through Pycharm IDE. 

In Topic-Specific PageRank Algorithm, the random walker does not teleport to any random 
node of a graph but to a specific set of nodes, for example the ones that are related 
to a specific topic. The formula for topic-specific pagerank is similar to the general 
pageRank formula. The following equation: βM + (1 − β)/|S| is used to calculate the 
Topic-Specific pageRank of the given graph. The above equation contains several variables
where S is a teleport set thats consists of pages we have identified as belonging to a 
certain topic. This project defined the topic set S to be {3,4} where nodes 3 and 4 belong 
to the same topic. Also, M is the transition matrix of the given graph, β (beta) is the probability
for each node's link to follow at random to the topic set nodes, and |S| is the size of set S. 

   
The tspr.py first creates the stochastic matrix M and intial rank vector (r0) using 
numpy.array(). It then sends the matrix M, r0, Beta β, e (stopping threshold), and the 
teleport set S to the method topic_specific_pagerank() as its parameters. This method uses
uses the topic-specific pagerank equation to calculate the pageRank of node in the given 
graph. It uses power iteration method by multiplying matrix M to the previous calculated 
rank vector (rOld) to create a new ranking vector (rNew). This power iteration process continues
until the rank vector (rNew) converges, in other words, the method keeps performing the power iteration 
until the length of the difference of new and old vector is less than the stoppig threshold (e). 
To calculate the absolute value of the difference between new and old rank vectors, and the sum their 
each element difference, the method topic_specific_pagerank() uses a helper method sum_of_diff(). 
Overall, the implementation has performed 19 power iterations until the converged rank vector is found.
This is the following converged rank vector that algorithm has calculated for the given graph and the stopping 
threshold (e = 0.01): 
0.058444	
0.119515	
0.219067	
0.181828	
0.058444	
0.146675	
0.118788	
0.097239	
