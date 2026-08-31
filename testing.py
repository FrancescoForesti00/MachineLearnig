#test usato per sperimentare

import numpy as np


losses = np.loadtxt('Losses//Stochastic_losses')
T = losses[0]
n = len(T)
print(n)
print(losses)