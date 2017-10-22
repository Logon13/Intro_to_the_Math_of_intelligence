from numpy import *

'''
Computes the error for a linear graph

y = mx + b

m = gradient
b = y-intercept
N = number of points

Error for individual point(x,y) = (y - (mx+b))^2
Error for all points = 1/N * Sum(Error for individual points) 
''' 
def computeError(b, m, points):
	totalError = 0
	
	#For each point
	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		totalError += (y - (m * x + b)) ** 2
	return totalError / float(len(points))

'''
Calculates the partial derivative with respect to m	
	
m = gradient
b = y-intercept
N = number of points

individual point caclulation(x,y) = -x(y - (mx + b))
derivative = 2/N * sum(individual point calculation)
'''
def computePartialDerivativeM(b, m, points):
	N = float(len(points))
	derivativeM = 0
	
	#For each point
	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		derivativeM += (x * (y - (m * x + b) ))
	
	return (-2/N) * derivativeM

'''
Calculates the partial derivative with respect to m	
	
m = gradient
b = y-intercept
N = number of points

individual point caclulation(x,y) = -(y-(mx+b))
derivative = 2/N * sum(individual point calculation)
'''
def computePartialDerivativeB(b, m, points):
	N = float(len(points))
	derivativeB = 0
	
	#For each point
	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		derivativeB += (y - (m * x + b))

	return (-2/N) * derivativeB
	
if __name__ == '__main__':
	points = genfromtxt("blood.csv", delimiter=",", skip_header=1)	
	
	learningRate = 0.0001 #The learning rate
	numberOfIterations = 1000 #The number of iterations
	b = 0 #initial value for b
	m = 0 #initial value for m
	
	for i in range(1000):
		#Update our values of b and m
		b = b - (learningRate * computePartialDerivativeB(b, m, points))
		m = m - (learningRate * computePartialDerivativeM(b, m, points))

	#Print out a summary
	print("y = " + format(m, '.2f') + "x + " + format(b, '.2f'))
	print("Error = " + str(computeError(b, m, points)))
