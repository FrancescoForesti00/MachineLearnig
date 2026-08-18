#Implementation from scratch of the hedge algorithm with a fixed learning rate


import math
import numpy as np

def algo():
    print('Configure Hedge Algorithm\n')

    print('Select losses type:\n1)Stochastic_losses\n2)Adversarial_losses\n3)Low-gap_losses\n')
    loss_choice = int(input())

    #learning rate selection
    #print('Select learning rate\n')
    learning_rate = 0.5#float(input())

    print('Enter the number K of desired experts\n')
    k =  int(input())

    print('Enter the number of turns T\n')
    T = int(input())


    #initialization TODO: implementare in modo che le losses vengano generate automaticamente qui? oppure mantengo le cose separate?
    index_selection = [i for i in range(k)]
    weights = [1 for i in range(k)]
    probabilities = [0 for i in range(k)]
    losses = np.loadtxt((loss_choice == 1)*'Stochastic_losses.txt' + (loss_choice == 2)*'Adversarial_losses.txt' + (loss_choice == 3)*'Low-gap_losses.txt', usecols=range(k))


    for t in range(T):
        somma = 0
        #define the distribution p
        for i in range(k):
            somma = somma + weights[i]
        for i in range(k):
            probabilities[i] = weights[i]/somma

        #draw I according to p
        chosen = np.random.choice(index_selection, None, True ,probabilities)
        print(chosen)
        #TODO decidere cosa salvarsi per il plot
        #update the weights
        for i in range(k):
            weights[i] = weights[i]*math.exp(-(learning_rate*losses[t][i]))



    #print(sum(weights))
    #print(sum(probabilities))