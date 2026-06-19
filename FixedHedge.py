import numpy as np

def algo():
    print('Configure Hedge Algorithm\n')
    #print('Select learning rate\n')
    #learning_rate = float(input())
    print('Enter the number K of desired experts\n')
    k =  int(input())
    #weights initialization
    index_selection = [i for i in range(k)]
    weights = [1 for i in range(k)]
    probabilities = [0 for i in range(k)]


    print('Enter the number of turns T\n')
    T = int(input())

    losses = [[]]
    losses = np.loadtxt('Stochastic_losses.txt', usecols=range(k))

    print(losses)
'''
    for t in range(T):
        somma = 0
        #calcola somma
        for i in range(k):
            somma = somma + weights[i]
        #calcola le probabilità
        for i in range(k):
            probabilities[i] = weights[i]/somma
        #scegli I
        choosen_index = np.random.choice(index_selection,probabilities)
        #recupera le loss


        for i in range(k):
            losses[i] =
        #aggiorna weights
        '''