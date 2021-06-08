<h1>Topic-Specific PageRank Algorithm</h1>

<p>This project implements Topic-Specific PageRank algorithm using Python. Please download the zipped folder 
and run the tspr.py file using Python IDE or through Pycharm IDE. 

In Topic-Specific PageRank Algorithm, the random walker does not teleport to any random 
node of a graph but to a specific set of nodes, for example the ones that are related 
to a specific topic. The formula for topic-specific pagerank is similar to the general 
pageRank formula. The following equation: βM + (1 − β)/|S| is used to calculate the 
Topic-Specific pageRank of the graph shown below </p>. ![alt text](https://github.com/madhupodugu/TopicSpecific-PageRankAlgorithm/blob/master/graph.JPG)

<p>This project has already defined the topic set S to be {3,4} where nodes 3 and 4 belong 
to the same topic. Also, M is the transition matrix of the given graph, β (beta) is the probability
for each node's link to follow at random to the topic set nodes, and |S| is the size of set S.</p> 
