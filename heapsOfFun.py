import math
import numpy as np
from read import getPoints

#Heap's algorith
bestTour = []
bestTourDst = math.inf

def generate(indices, n):
	if(n == 1):
		evaluateSolution(indices)
	else:
		for i in range(n):
			generate(indices, n - 1)
			swapIndex = i
			if n % 2 == 0:
				swapIndex = i
			else:
				swapIndex = 0
			indices[swapIndex], indices[n - 1] = indices[n-1], indices[swapIndex] 

def evaluateSolution(indices):
	global bestTour
	global bestTourDst

	n = len(indices)
	if(indices[0] < indices[n - 2]):
		tour = 0
		n = len(indices)
		
		for i in range(n):
			if i + 1 == n:
				tour += distance(indices[i], indices[0])
			else:
				tour += distance(indices[i], indices[i + 1])

		if tour < bestTourDst:
			bestTourDst = tour
			bestTour = indices

def distance(i, j):
	return dist_matrix[i][j]

#List of points
points = getPoints()
n = len(points)
indices = list(range(len(points)))

dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i][j] = np.linalg.norm(np.array(points[i]) - np.array(points[j]))

generate(indices, len(indices))
print(bestTour)
print(bestTourDst)