import random
import itertools
import collections
import numpy as np
from matrix import Matrix


def all_edges(n):
    return list(itertools.combinations(range(1,n+1), 2))

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

def a_tournament(edges, k):
    if k == 0:
        return edges
    elif k%2 == 0:
       return [edges[0]] + a_tournament(edges[1:len(edges)], k//2) 
    else:
       return flip([edges[0]]) + a_tournament(edges[1:len(edges)], k//2)

#generates all tournaments on n vertices    
def all_tournaments(n):
    edges = all_edges(n)
    return map(lambda k: a_tournament(edges,k), range(0,2**(n*(n-1)//2)))

#returns a histogram of Hamiltonian path numbers and the number of occurences 
def hamiltonian_path_counts(histogram):
    return sorted(collections.Counter(histogram).items())

def random_hamiltonian_histogram(n, sampleSize):
    hamiltonian_list = []
    for i in range(sampleSize):
        hamiltonian_list.append(count_hamiltonian_paths(random_tournament(n), n))
    hamiltonian_list.sort()
    return hamiltonian_list, hamiltonian_path_counts(hamiltonian_list)

def hamiltonian_histogram(n):
    histogram = map(lambda tournament: count_hamiltonian_paths(tournament, n), all_tournaments(n))
    histogram.sort()
    return histogram, hamiltonian_path_counts(histogram)

def balance_edge(edge, n):
    (i,j) = edge
    if 2*((i-j)%n) < n:
        return edge
    else:
        return (j,i)

def balanced_tournament(n):
    return list(map(lambda edge: balance_edge(edge, n), all_edges(n)))


def record_count(n):
    current_record = 0
    for tournament in all_tournaments(n):
        number_of_hamiltonian_paths = count_hamiltonian_paths(tournament, n)
        if number_of_hamiltonian_paths >= current_record:
            current_record = number_of_hamiltonian_paths
            print('Number of paths:', current_record)
            print(tournament)

print(record_count(6))



# randlist, randcounts = random_hamiltonian_histogram(6,10000)
# hamlist, hamcounts = hamiltonian_histogram(6)
#print(hamlist)
#print(hamcounts)
#print(randlist)
#print(randcounts)
# print('\n'.join(map(str, hamcounts)))
# print('\n'.join(map(str, randcounts)))









# TO DO:
#
# Hamiltonian cycles
# 1 Factors
# length of longest cycle
