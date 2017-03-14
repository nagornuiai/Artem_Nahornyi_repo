def cost_func(x, y, theta, alpha):
    
    J = (1/(2*len(y))) * np.sum( np.power((x*theta - y), 2) , axis = 0)
    
    return J

def gradient_func(x, y, theta, alpha, num_iter):
    i = 0
    J_hist = np.array([])
    while i < num_iter:
        
        theta = theta - np.transpose(alpha * (1/len(y)) * np.sum( np.multiply((x*theta - y), x), axis = 0))
        i += 1
        J = cost_func(x, y, theta, alpha)
        J_hist = np.append(J_hist, J)
        
    return (J_hist, theta)

def normalize_func(x):
    
    mu = x.mean(0)
    sigma = x.std(0)
    x_norm = (x - mu)/sigma
    
    return (x_norm, mu, sigma)


#############################################


import numpy as np
import matplotlib.pyplot as plt

fhand = open('ex1data2.txt', 'r')


data = list()
data = np.array([int(data) for line in [line.strip().split(',') for line in fhand] for data in line])
Len = int(len(data)/3)
data = np.matrix(data)
data = data.reshape(Len, 3)


x = data[:,0:2]
y = data[:,-1]
theta = np.matrix([[0],[0],[0]])
num_iter = 400
alpha = 0.1

(x, mu, sigma) = normalize_func(x)
 
x = np.concatenate((np.ones([Len,1]), x), axis = 1)

(J_hist, theta) = gradient_func(x, y, theta, alpha, num_iter)

plt.plot(np.arange(1,401), J_hist)
plt.show

est = input('>>\n')
est = np.matrix([int(n) for n in est.strip().split(',')])

output = np.hstack((np.ones((1,1)), ((est - mu)/sigma))) * theta

print(output)