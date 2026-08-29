#Implementation from scratch of the adaptive hedge algorithm with a dynamic learning rate


import math
import numpy
import numpy as np
import matplotlib.pyplot as plt

from DatasetGeneration import losses


def algo():
    print('Configure Adaptive Hedge Algorithm\n')

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
        return

    #initialization
    delta = 0
    psi = 1.62
    budget = 0
    learning_rate = psi
    index_selection = [i for i in range(k)]
    weights = [1 in range(k)]
    probabilities = [0 in range(k)]
    regret = [0 in range(T)]
    cumulative_loss = [0] * T
    expert_losses = [0 in range(k)]

    for t in range(T):
        #if is the first round or the cumulative mixabilty gap exceeded the budget
        if(t ==0 or delta >= budget):
            #start new segment
            #update learning rate, budget, cumulative mixabilty gap, weights vector
            learning_rate = learning_rate/psi
            budget = (1/(math.e - 1) + 1/learning_rate)*math.log(k)
            delta = 0
            weights = [1/k in range(k)]

        #make a decision

        #prepare for next round
        #update the value of  the cumulative mixabilty gap TODO: check che funzioni
        delta = delta + numpy.inner(weights, losses[t]) + 1/learning_rate * math.log(weights * math.exp(-learning_rate * loss))
        #update weights vector TODO: check che funzioni
        weights = numpy.inner(weights, math.exp(-learning_rate * losses[t]))/(weights * math.exp(-learning_rate * loss))





        somma = 0
        #define the distribution p
        for i in range(k):
            somma = somma + weights[i]
        for i in range(k):
            probabilities[i] = weights[i]/somma

        #draw I according to p
        chosen = np.random.choice(index_selection, None, True ,probabilities)


        #cumulative loss update
        cumulative_loss[t] = cumulative_loss[t - 1] + losses[t][chosen]

        #expert losses update
        for i in range(k):
            expert_losses[i] = expert_losses[i] + losses[t][i]

        # regret
        regret[t] = cumulative_loss[t]/(t + 1) - min(expert_losses)/(t + 1)

        #update the weights
        for i in range(k):
            weights[i] = weights[i]*math.exp(-(learning_rate*losses[t][i]))

    print(regret[T - 1])
    print(min(expert_losses))
    print(cumulative_loss[T - 1])


    plt.plot([(i + 1) for i in range(T)], cumulative_loss, "b-", label= "cumulative loss")
    plt.plot( [(i + 1) for i in range(T)], regret, "r.", label = "regret")
    plt.legend(loc = 'upper left')
    plt.show()