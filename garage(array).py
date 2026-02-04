def garage(initial, final):

    initial = initial[::]      # prevent changes in original 'initial'
    seq = []                   # list of each step in sequence
    steps = 0
    while initial != final:
        zero = initial.index(0)
        if zero != final.index(0):  # if zero isn't where it should be,
            car_to_move = final[zero]   # what should be where zero is,
            pos = initial.index(car_to_move)         # and where is it?
            initial[zero], initial[pos] = initial[pos], initial[zero]
        else:
            for i in range(len(initial)):
                if initial[i] != final[i]:
                    initial[zero], initial[i] = initial[i], initial[zero]
                    break
        seq.append(initial[::])
        steps += 1

    return steps, seq       
    # e.g.:  4, [{0, 2, 3, 1, 4}, {2, 0, 3, 1, 4}, 
    #            {2, 3, 0, 1, 4}, {0, 3, 2, 1, 4}]
initial = [1, 2, 3, 0, 4]
final   = [0, 3, 2, 1, 4]

steps, seq = garage(initial, final)

print("Steps =", steps)
print("Sequence:",seq)