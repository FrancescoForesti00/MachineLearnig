#Implementation from scratch of the hedge algorithm with a fixed learning rate


import math
import numpy as np
import matplotlib.pyplot as plt

#TODO funziona troppo bene evidentemente c'è qualcosa di sbagliato (probabilità selezione, modo in cui vengono conteggiati cumulative losses/regret...)


def algo():
    print('Configure Hedge Algorithm\n')

    print('Select losses type:\n1)Stochastic_losses\n2)Adversarial_losses\n3)Low-gap_losses\n')
    loss_choice = int(input())

    print('Enter the number K of desired experts\n')
    k = int(input())

    print('Enter the number of turns T\n')
    T = int(input())

    if loss_choice == 1:
        losses = np.loadtxt((loss_choice == 1) * 'Stochastic_losses', usecols=range(k))
    elif loss_choice == 2:
        losses = np.loadtxt((loss_choice == 2) * 'Adversarial_losses', usecols=range(k))
    elif loss_choice == 3:
        losses = np.loadtxt((loss_choice == 3) * 'Low-gap_losses', usecols=range(k))
    else:
        print('Invalid choice')

    #learning rate selection
    #print('Select learning rate\n')
    learning_rate = 0.5#float(input())




    #initialization
    index_selection = [i for i in range(k)]
    weights = [1 for i in range(k)]
    probabilities = [0 for i in range(k)]
    regret = [0] * T
    cumulative_loss = [0] * T
    expert_losses = [0 for i in range(k)]


    print(regret)
    print(cumulative_loss)

    for t in range(T):
        somma = 0
        #define the distribution p
        for i in range(k):
            somma = somma + weights[i]
        for i in range(k):
            probabilities[i] = weights[i]/somma

        #draw I according to p
        chosen = np.random.choice(index_selection, None, True ,probabilities)


        #cumulative loss update
        cumulative_loss[t] = cumulative_loss[t-1] + losses[t][chosen]

        #expert losses update
        for i in range(k):
            expert_losses[i] = expert_losses[i] + losses[t][i]

        # regret
        regret[t] = cumulative_loss[t]/(t + 1) - min(expert_losses)/(t + 1)

        #update the weights
        for i in range(k):
            weights[i] = weights[i]*math.exp(-(learning_rate*losses[t][i]))

    print(regret)
    print(cumulative_loss)

    #plot TODO migliorare data visualization
    plt.plot([(i + 1) for i in range(T)], cumulative_loss, "b-", [(i + 1) for i in range(T)], regret, "r.")
    plt.show()