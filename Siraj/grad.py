# -*- coding: utf-8 -*-

from numpy import *

    #Step 1 - Collect Data
    points = genfromtxt('data.csv', delimiter=',')
    
    #Step 2 - define our hyperparameters
    #how fast should our model converge?
    learning_rate = 0.0001
    #y = mx + b (slope formula)
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    
    #Step 3 - train our model
    print 'starting gradient descent at b = {0} , m ={1}, error = {2}'.format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points))
    [b , m] gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_interations)
    print 'ending point at .b = {1} , m ={2}, error = {3}'.format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points))
    
if __main__ == '__main__':
    run()
    