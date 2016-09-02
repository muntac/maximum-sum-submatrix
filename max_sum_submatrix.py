import csv 
import sys
import copy

matrix = []
cumulative_matrix = []
N = 0

def read_input():
    global N,  matrix, cumulative_matrix
    with open ('matrix.csv', 'rb') as csvfile:	
	matrixreader = csv.reader(csvfile, delimiter=',')
	for row in matrixreader:
	    matrix.append([])
	    for col in row:
		matrix[N].append(col)
	    N += 1
	for i in range(0, N):
	    for j in range(0, N):
		matrix[i][j] = int(matrix[i][j])
	cumulative_matrix = copy.deepcopy(matrix)

def matrix_value(i, j):
    global cumulative_matrix
    if(i < 0 or j < 0 or i > N - 1 or j > N - 1):
        return 0
    else:
        return cumulative_matrix[i][j] 
    
def calculate_cumulative():
    global cumulative_matrix
    global matrix
    for y in range(0, N):
	for x in range(0, N):
	    cumulative_matrix[x][y] = matrix_value(x - 1, y) + matrix_value(x, y - 1) + matrix_value(x, y) - matrix_value(x - 1, y - 1)

def matrix_sum(i, j, k, l):
    return matrix_value(k, l) - matrix_value(k, j - 1) - matrix_value(i - 1, l) + matrix_value(i - 1, j - 1) 

def find_max_sub_matrix():
    global matrix
    max_i = -1
    max_j = -1
    max_k = -1
    max_l = -1
    max_matrix_sum = -sys.maxint - 1

    for i in range(0, N):
	for j in range(0, N):
	    for k in range(i, N):
		for l in range(j, N):
		    current_sum = matrix_sum(i, j, k, l) 
		    if(current_sum > max_matrix_sum):
			max_matrix_sum = current_sum
			max_i = i
			max_j = j
			max_k = k
			max_l = l

    max_sub_matrix = []
    for x in range(max_i, max_k + 1):
	row = []
	for y in range(max_j, max_l + 1):
	    row.append(matrix[x][y])
	max_sub_matrix.append(row)
    print "Max Submatrix"
    for row in max_sub_matrix:
        print row
    print "Submatrix Sum: %d" % max_matrix_sum

#--MAIN--#
read_input()
calculate_cumulative()
find_max_sub_matrix()

