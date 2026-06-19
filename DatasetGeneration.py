import random

import numpy as np

print('select which dataset you want to generate\n1)Stochastic\n2)Adversarial\n3)Low-gap\n')

choice = input()

if choice == '1':
    print('Select the number of experts(one will have Bernoulli(0.3) the others Bernoulli(0.5))\n')
elif choice == '2':
    print('Select the number of experts(the best one will change over time)\n')
elif choice == '3':
    print('Select the number of experts(one will have Bernoulli(0.49) the others Bernoulli(0.5))\n')
else:
    print('ERROR\n')

k: int = int(input())
print('Select the number of turns\n')
T: int = int(input())

losses = [[9]*k]*T
loss_probability = [0]*k
rng = np.random.default_rng()

if choice == '1':

    for i in range(k):
        if i == 0:
            loss_probability[i] = 0.3
        else:
            loss_probability[i] = 0.5
    losses = rng.binomial(1, loss_probability, size=(T, k))

elif choice == '2':
    for t in range(T):
        #select one of the experts to be the best
        best_of_turn = random.randint(0, k-1)
        for i in range(k):
            if i == best_of_turn:
                loss_probability[i] = 0.3
            else:
                loss_probability[i] = 0.5

            losses[t][i] = int(rng.binomial(1, loss_probability[i], size=()))


elif choice == '3':
    for i in range(k):
        if i == 0:
            loss_probability[i] = 0.49
        else:
            loss_probability[i] = 0.5
    losses = rng.binomial(1, loss_probability, size=(T, k))

#stampa su di un file
with open((choice =='1')*'Stochastic_losses.txt' + (choice == '2')*'Adversarial_losses' + (choice == '3')*'Low-gap_losses', 'w') as f:
    for t in losses:
        f.write(' '.join([str(a) for a in t]) + '\n')




