import itertools


for i in range(1, 4):
    bouquets_iter = itertools.combinations(flower_names, i)
    for bouquet in bouquets_iter:
        print(bouquet)
