from formulaction import data_to_matrix, ising_params
import ising

cnf = [[1,2], [2,3], [1,-2],[2,-1]]

n = 3 
m = len(cnf)

matrix = data_to_matrix(m, n, cnf)

J,h = ising_params(m, n, matrix)

graph  = { (i,i): k for i, k in enumerate(h) }


J2 = {}
for i, x in enumerate(J):
    for j, m in enumerate(x):
        if m !=0:
            graph[(i,j)] = m


result = ising.search(graph, num_states=8)
print(result.energies)