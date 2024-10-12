import numpy as np

# Define the points
points = [(100, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (10, 2), (90, 2)]
numPoints = len(points)

# Calculate the distance matrix
distMatrix = np.zeros((numPoints, numPoints))
for i in range(numPoints):
    for j in range(numPoints):
        distMatrix[i][j] = np.linalg.norm(np.array(points[i]) - np.array(points[j]))

# ACO parameters
numAnts = 10
numIterations = 100
evaporationRate = 0.5
alpha = 1  # Importance of pheromone
beta = 2   # Importance of distance

# Initialize pheromones
pheromones = np.ones((numPoints, numPoints))

# Function to calculate the probability of moving to the next point
def calculateProbabilities(currentPoint, visited):
    probabilities = []
    for i in range(numPoints):
        if i not in visited:
            prob = (pheromones[currentPoint][i] ** alpha) * ((1.0 / distMatrix[currentPoint][i]) ** beta)
            probabilities.append(prob)
        else:
            probabilities.append(0)
    return probabilities / np.sum(probabilities)

# Main ACO loop
bestRoute = None
bestDistance = float('inf')

for iteration in range(numIterations):
    allRoutes = []
    allDistances = []
    
    for ant in range(numAnts):
        visited = [0]
        currentPoint = 0
        routeDistance = 0
        
        while len(visited) < numPoints:
            probabilities = calculateProbabilities(currentPoint, visited)
            nextPoint = np.random.choice(range(numPoints), p=probabilities)
            routeDistance += distMatrix[currentPoint][nextPoint]
            visited.append(nextPoint)
            currentPoint = nextPoint
        
        routeDistance += distMatrix[currentPoint][0]  # Return to start
        allRoutes.append(visited)
        allDistances.append(routeDistance)
        
        if routeDistance < bestDistance:
            bestDistance = routeDistance
            bestRoute = visited
    
    # Update pheromones
    pheromones *= (1 - evaporationRate)
    for route, distance in zip(allRoutes, allDistances):
        for i in range(numPoints - 1):
            pheromones[route[i]][route[i + 1]] += 1.0 / distance
        pheromones[route[-1]][route[0]] += 1.0 / distance
#shows points rather then index
for i in range(numPoints):
    bestRoute[i] = int (bestRoute[i])
    
print("Best route:", bestRoute)
print("Best distance:", bestDistance)
