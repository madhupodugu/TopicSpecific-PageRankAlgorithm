import numpy as np

def topic_specific_pagerank(A, beta, S, r0, e):
    bA = np.multiply(A, beta) #M*0.8
    my_print("\nbA:", bA)

    s = np.array([[0],[0],[1],[1],[0],[0],[0],[0]])#vector that has 1 in the components in S
    t = round((1-beta)*1/len(S), 2) #1-beta/|S|
    v = np.multiply(s, t)
    my_print("\n(1-beta)s/|S|: ", v)
    a = bA + v #v' matrix
    my_print("\nbA + v: ", a)

    print("Starting Power Iteration...\n")

    #Calculating r1: a*r0
    #dot() is an in-built numpy function for calculating matrix-vector products
    r1 = a.dot(r0)
    r_O = r1 #r_O will be used to calculate next rNew
    Sum = sum_of_diff(r1, r0)
    print("Sum: ", Sum)
    my_print("1st iteration: ", r1)
    iteration = 2

    #Performing Power Iteration until convergence
    while(Sum > e ):
        r_N = a.dot(r_O)
        p = str(iteration) + " iteration"
        my_print(p, r_N)
        Sum = sum_of_diff(r_N, r_O)
        print("Sum: ", Sum, "\n")
        if(Sum > e):
            r_O = r_N
        iteration = iteration+1

#Calculates the absolute value of the difference between new and old rank vectors and adds that difference to a running sum
def sum_of_diff(rNew, rOld):
    sum = 0.0
    for i in range(0, 8):
        d = abs(rNew[i] - rOld[i])
        sum = sum + d
    return sum

#Prints the numpy array in a clean matrix format and rounds the array float values to 6 decimal places
def my_print(prompt, x):
    print(prompt)
    for row in x:
        print(' '.join(map(lambda x: "{:.6f}\t".format(x), row)))


#Creating Stochastic Matrix of the given graph
M = np.array([[0,0,1/3,0,0,0,0,0],[1,0,0,1/2,0,0,0,0],[0,1,0,0,1/2,0,0,0],[0,0,1/3,0,1/2,0,0,0],
           [0,0,1/3,0,0,0,0,0],[0,0,0,1/2,0,0,0,1],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0]])
Beta = 0.8
S = [3,4]#topic teleport set
r0 = np.array([[0],[0],[1/2],[1/2],[0],[0],[0],[0]])#intial rank vector
e = 0.01 #stopping threshold
print("r0: \n", r0)

my_print("\nIntial Matrix: ", M)

topic_specific_pagerank(M, Beta, S, r0, e)