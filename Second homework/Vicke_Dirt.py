import numpy as np
import matplotlib.pyplot as plt

nCoupledOscillators = 10
theta = (np.random.rand(nCoupledOscillators)-0.5)*np.pi/2
omega = np.random.standard_cauchy(nCoupledOscillators)

dt = 0.01
tmax = 1

for t in range(tmax/dt):
    for i in range(nCoupledOscillators):
