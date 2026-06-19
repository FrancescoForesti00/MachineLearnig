from Models import FixedHedge,AdaptiveHedge


print('Welcome\nSelect which set of losses you want to use:\n-Stochastic\n-Adversarial\n-Low-Gap\n')
n = input()

if n == 'hedge':
    FixedHedge.algo()

else:
    print('unrecognized command')


"adaptiveEdge = AdaptiveHedge()"


