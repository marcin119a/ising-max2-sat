import numpy as np

def data_to_matrix(m, n, data):
    matrix = np.zeros((m, n), dtype=np.int32)
    for j in range(m):
        var1, var2 = data[j][0], data[j][1]
        matrix[j][abs(var1)-1] = var1//abs(var1)
        matrix[j][abs(var2)-1] = var2//abs(var2)
    return matrix


def ising_params(m, n, matrix):
    
    """ Encoding SAT matrix to Ising 2-body Hamiltonian folowing 
        S.Santra et al. Max 2-SAT with up to 108 qubits (2014).
        Author: Арсен Кужамуратов <kyzhamuratov_arsen@mail.ru>    
    """ 
    
    v = np.zeros((m, n),dtype=np.int32)
    for i in range(m):
        expr = matrix[i]
        for index, k in enumerate(expr):
            if k!=0: v[i,index] = k//abs(k) 
                
    # constructing Ising matrix and biases
    J = np.zeros((n, n), dtype=np.float32)
    h = np.zeros(n,dtype=np.float32)
    
    for j in range(m):
        index1 = -1
        index2 = 0
        for i in range(n):
            if v[j,i]!=0 and index1==-1:
                index1 = i+1
                continue
            if v[j,i]!=0 and index1!=0: 
                index2 = i+1
                break
        J[index1-1,index2-1] += v[j,index1-1]*v[j,index2-1]
        h[index1-1] += -v[j,index1-1] 
        h[index2-1] += -v[j,index2-1]  
    return J, h
