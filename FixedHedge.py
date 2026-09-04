#Implementation from scratch of the hedge algorithm with a fixed learning rate


import math
import numpy as np
import matplotlib.pyplot as plt




def algo():
    print('Configure Hedge Algorithm\n')

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

    #learning rate selection
    print('Select learning rate\n')
    learning_rate = float(input())


    k = len(losses[0])
    t_max = len(losses)


    #select number of iterations
    print("How many iterations would you like to run?\n")
    n = int(input())
    all_regrets = [[0]*t_max for _ in range(n)]
    all_cumulative_losses = [[0]*t_max for _ in range(n)]

    for s in range(n):
        #initialization
        index_selection = [i for i in range(k)]
        weights = [1.0] * k
        probabilities = [0.0] * k
        expert_losses = [0] * k

        #iteration of the algorithm
        for t in range(t_max):
            #define the distribution p
            somma = sum(weights)
            for i in range(k):
                probabilities[i] = weights[i]/somma

            #draw I according to p
            chosen = np.random.choice(index_selection, None, True ,probabilities)


            #cumulative loss update
            if t == 0:
                all_cumulative_losses[s][t] = losses[t][chosen]
            else:
                all_cumulative_losses[s][t] = all_cumulative_losses[s][t - 1] + losses[t][chosen]

            #expert losses update
            for i in range(k):
                expert_losses[i] = expert_losses[i] + losses[t][i]

            # regret
            all_regrets[s][t] = all_cumulative_losses[s][t] - min(expert_losses)

            #update the weights
            for i in range(k):
                weights[i] = weights[i]*math.exp(-(learning_rate*losses[t][i]))

    #calculate the mean
    regret = [0.0]*t_max
    cumulative_loss = [0.0]*t_max


    for t in range(t_max):
        for i in range(n):
            regret[t] = regret[t] + all_regrets[i][t]
            cumulative_loss[t] = cumulative_loss[t] + all_cumulative_losses[i][t]
        regret[t] = regret[t]/n
        cumulative_loss[t] = cumulative_loss[t]/n

    print(regret[t_max - 1])
    #print(min(expert_losses))
    print(cumulative_loss[t_max - 1])

    plt.grid(True)
    plt.xlabel('Turns')
    plt.plot(cumulative_loss[::100], "b-", label= "cumulative loss")
    plt.plot( regret[::100], "ro-", label = "regret")
    plt.legend(loc = 'lower right')
    plt.show()