import numpy as np

print('select which dataset you want to generate\n1)Stochastic\n2)Adversarial\n3)Low-gap\n')

choice = input()

if choice == '1':
    print('Select the number of experts(one will have Bernoulli(0.3) the others Bernoulli(0.5))\n')
if choice == '2':
    print('Select the number of experts(the best one will change over time)\n')
if choice == '3':
    print('Select the number of experts(one will have Bernoulli(0.49) the others Bernoulli(0.5))\n')
else:
    print('ERROR\n')



k = int(input())
print('Select the number of turns\n')
T = int(input())