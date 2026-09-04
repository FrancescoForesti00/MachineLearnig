#Implementation from scratch of the adaptive hedge algorithm with a dynamic learning rate

import math
import numpy
import numpy as np
import matplotlib.pyplot as plt




def algo():
    print('Configure Adaptive Hedge Algorithm\n')

    print('Select losses type:\n1)Stochastic_losses\n2)Adversarial_losses\n3)Low-gap_losses\n')
    loss_choice = int(input())


    if loss_choice == 1:
        losses = np.loadtxt((loss_choice == 1) * 'Losses//Stochastic_losses')
    elif loss_choice == 2:
        losses = np.loadtxt((loss_choice == 2) * 'Losses//Adversarial_losses')
    elif loss_choice == 3:
        losses = np.loadtxt((loss_choice == 3) * 'Losses//Low-gap_losses')
    else:
        print('Invalid choice')
        return
    print("Computing...\n")
    k = len(losses[0])
    t_max = len(losses)

    # select number of iterations
    print("How many iterations would you like to run?\n")
    n = int(input())
    all_regrets = [[0] * t_max for _ in range(n)]
    all_cumulative_losses = [[0] * t_max for _ in range(n)]


    for s in range(n):
        # initialization
        counter = 1
        delta = 0
        psi = 2
        budget = 0
        learning_rate = psi
        index_selection = [i for i in range(k)]
        weights = [1 / k] * k
        probabilities = [0.0] * k
        expert_losses = [0] * k

        # iteration of the algorithm
        for t in range(t_max):
            #if is the first round or the cumulative mixability gap exceeded the budget
            if t == 0 or delta >= budget:
                if t==0:
                    counter = 1
                else:
                    counter = counter + 1

                ##start new segment
                #update learning rate, budget, cumulative mixability gap, weights vector
                learning_rate = learning_rate/psi
                budget = (1/(math.e - 1) + 1/learning_rate)*math.log(k)
                delta = 0
                weights = [1/k] * k

            ##make a decision

            # define the distribution p
            somma = sum(weights)

            for i in range(k):
                probabilities[i] = weights[i]/somma

            # draw I according to p
            chosen = np.random.choice(index_selection, None, True, probabilities)

            # cumulative loss update
            if t==0:
                all_cumulative_losses[s][t] = losses[t][chosen]
            else:
                all_cumulative_losses[s][t] = all_cumulative_losses[s][t-1] + losses[t][chosen]

            #expert losses update
            for i in range(k):
                expert_losses[i] = expert_losses[i] + losses[t][i]

            # regret
            all_regrets[s][t] = all_cumulative_losses[s][t] - min(expert_losses)


            ##prepare for next round

            #update the value of  the cumulative mixabilty gap(delta grande)
            log_argument = 0
            for i in range(k):
                log_argument = log_argument + weights[i] * math.exp(-learning_rate * losses[t][i])
            delta = delta + numpy.inner(weights, losses[t]) + 1/learning_rate * math.log(log_argument)

            #update weights vector
            for i in range(k):
                weights[i] = weights[i] * math.exp(- learning_rate * losses[t][i])/log_argument

        print(counter, "\n")

    # calculate the mean
    regret = [0.0]*t_max
    cumulative_loss = [0.0]*t_max


    for t in range(t_max):
        for i in range(n):
            regret[t] = regret[t] + all_regrets[i][t]
            cumulative_loss[t] = cumulative_loss[t] + all_cumulative_losses[i][t]
        regret[t] = regret[t]/n
        cumulative_loss[t] = cumulative_loss[t]/n

    print(regret[t_max - 1])
    print(cumulative_loss[t_max - 1])

    plt.grid(True)
    plt.xlabel('Turns')
    plt.plot( regret[::100], "ro-", label = "regret")
    plt.plot(cumulative_loss[::100], "b-", label="cumulative loss")
    plt.legend(loc='upper left')
    plt.show()



