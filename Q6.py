import numpy as np
bib_numbers=np.array([101, 102, 103, 104, 105, 106])
times_5k=np.array([22.3, 25.1, 21.8, 26.4, 23.0, 24.7])
bib_numbers_2=np.array([107, 108])
times_5k_2=np.array([20.5, 27.9])
#1
bib_numbers=np.concatenate((bib_numbers, bib_numbers_2))
times_5k=np.concatenate((times_5k, times_5k_2))
#2
rng=np.random.default_rng(42)
indices=rng.permutation(len(bib_numbers))
bib_numbers=bib_numbers[indices]
times_5k=times_5k[indices]
#3
order=np.argsort(times_5k)
ranked_bibs=bib_numbers[order]
ranked_times=times_5k[order]
for rank, (bib,time) in enumerate(
    zip(ranked_bibs, ranked_times), start=1
):
    print(rank,bib,time)
#4
rank_104 = np.where(ranked_bibs == 104)[0][0]+1
print("Bib 104 rank:", rank_104)