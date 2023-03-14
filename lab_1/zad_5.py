tab = [[5,3,2], [7,3,5], [-4,-9,-2], [-3,-4,-5]]
for w in tab:
    min_wart = min(w)
    min_ind = w.index(min_wart)
    w[0], w[min_ind] = w[min_ind], w[0]
print(tab)