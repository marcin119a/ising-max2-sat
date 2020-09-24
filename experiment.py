from formulaction import data_to_matrix, ising_params


cnf = [[1,2], [2,3], [1,-2],[2,-1]]

n = 3 
m = len(cnf)

matrix = data_to_matrix(m, n, cnf)

J,h = ising_params(m, n, matrix)
print(J)