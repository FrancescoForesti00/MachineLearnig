import FixedHedge

print('Welcome!!!\nSelect which algorithm you want to use:\nhedge\nadaptive_hedge\n')
choice = input()

if choice == 'hedge':
    FixedHedge.algo()
elif choice == 'adaptive_hedge':
    print('adaptive_hedge')
else:
    print('Error\n')
