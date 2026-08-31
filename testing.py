#test usato per sperimentare

import numpy as np


losses = np.loadtxt('Losses//Stochastic_losses')

n = len(losses[0])
T = len(losses)
print(T)
