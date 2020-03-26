import random
import itertools
import numpy
from matrix import Matrix

def pairs_that_start_with(first_value,upper_bound):
    return map(lambda x: (first_value,x), range(first_value+1,upper_bound))

def all_pairs(n):
    list_of_list = map(lambda x: pairs_that_start_with(x,n+1), range(1,n))
    return reduce(list.__add__, list_of_list)


#def flip(edges, index):
#    for i in range(0,len(edges)):
#        if index >> i & 1 == 1:
#            (a,b) = edges[i]
#            edges[i] = (b,a)
#    return edges

def remove_visited_edges(edges, v):
    return filter(lambda (a,b): (a != v) & (b != v), edges)

def edges_starting_with(edges, v):
    return filter(lambda (a,b): a == v, edges)

def count_hamiltonian_paths_starting_with(edges, v, counter):
    if counter == 0:
        return 1
    else:
        running_sum = 0
        for (a,b) in edges_starting_with(edges, v):
            running_sum += count_hamiltonian_paths_starting_with(remove_visited_edges(edges, v), b, counter-1)
        return running_sum

# counts the number of Hamiltonian paths in a tournament on n vertices
# with the given orientations

def count_hamiltonian_paths(edges, n):
    return sum(map(lambda i: count_hamiltonian_paths_starting_with(edges, i, n-1), range(1,n+1)))

# simulates n coin flips
def coinToss(n):
    recordList = []
    for i in range(n):
         flip = random.randint(0, 1)
         if (flip == 1):
              recordList.append(1)
         else:
              recordList.append(0)
    return recordList

# flips every ordered pair in a list
def flip(edges):
    flipped_edges = []
    for i in range(0,len(edges)):
        (a,b) = edges[i]
        flipped_edges.append((b,a))
    return flipped_edges

#generates a random tournament on n vertices
def random_tournament(n):
    pairs = list(itertools.combinations(range(1,n+1), 2))
    pairs_flipped = flip(pairs)
    edge_size = len(pairs)
    orientations = coinToss(edge_size)
    randTournament = []
    for i in range(len(pairs)):
        if(orientations[i] == 1):
            randTournament.append(pairs[i])
        else:
            randTournament.append(pairs_flipped[i])
    return randTournament

def hamiltonian_Histogram(n, sampleSize):
    hamiltonianList = []
    for i in range(sampleSize):
        hamiltonianList.append(count_hamiltonian_paths(random_tournament(n), n))
    hamiltonianList.sort()
    return hamiltonianList


print(Matrix(10, random_tournament(10)).adj)
#print hamiltonian_Histogram(10,30)





# TO DO:
#
# Hamiltonian cycles
# 1 Factors
# length of longest cycle
