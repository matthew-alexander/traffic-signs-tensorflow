"""
Have fun with the number of epochs!

Be warned that if you increase them too much,
the VM will time out :)
"""

import numpy as np
from miniflow import *

inputs, weights, bias = Input(), Input(), Input()

x = np.array([[-1., -2.], [-1, -2]])
w = np.array([[random.random(), random.random()], [random.random(), random.random()]])
b = np.array([random.random(), random.random()])
ideal_output = np.array(
    [[1.23394576e-04, 9.82013790e-01],
    [1.23394576e-04, 9.82013790e-01]])

f = Linear(inputs, weights, bias)
g = Sigmoid(f)
cost = MSE(g)

feed_dict = {inputs: x, weights: w, bias: b}

train_SGD(feed_dict, ideal_output, [weights, bias], 1000)