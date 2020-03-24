
def pairs_that_start_with(first_value,upper_bound):
    return map(lambda x: (first_value,x), range(first_value+1,upper_bound))

def all_pairs(n):
    list_of_list = map(lambda x: pairs_that_start_with(x,n+1), range(1,n))
    return reduce(list.__add__, list_of_list)


def flip(edges, index):
    for i in range(0,len(edges)):
        if index >> i & 1 == 1:
            (a,b) = edges[i]
            edges[i] = (b,a)
    return edges

#print flip(all_pairs(3), 0)

# number of Hamiltonian paths, number of Hamiltonian cycles, find the longest cycle

def remove_visited_edges(edges, v):
    return filter(lambda (a,b): (a != v) & (b != v), edges)

#print remove_visited_edges(flip(all_pairs(3), 0), 3)

def edges_starting_with(edges, v):
    return filter(lambda (a,b): a == v, edges)

#print edges_starting_with([(1,2), (1,3), (3,1), (10,2)], 2)

def count_hamiltonian_paths_starting_with(edges, v, counter):
    if counter == 0:
        return 1
    else:
        running_sum = 0
        for (a,b) in edges_starting_with(edges, v):
            running_sum += count_hamiltonian_paths_starting_with(remove_visited_edges(edges, v), b, counter-1)
        return running_sum

def count_hamiltonian_paths(edges, n):
    return sum(map(lambda i: count_hamiltonian_paths_starting_with(edges, i, n-1), range(1,n+1)))

print count_hamiltonian_paths([(1,2),(1,3),(2,3),(3,4),(4,2),(4,1)], 4)

print count_hamiltonian_paths_starting_with([(1,2),(1,3),(2,3),(3,4),(4,2),(4,1)], 1, 3)
print count_hamiltonian_paths_starting_with([(1,2),(1,3),(2,3),(3,4),(4,2),(4,1)], 2, 3)
print count_hamiltonian_paths_starting_with([(1,2),(1,3),(2,3),(3,4),(4,2),(4,1)], 3, 3)
print count_hamiltonian_paths_starting_with([(1,2),(1,3),(2,3),(3,4),(4,2),(4,1)], 4, 3)
