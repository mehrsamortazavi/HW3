import numpy as np
scores = np.array([
[18, 15, 20],
[12, 14, 16],
[20, 19, 18],
[10, 8, 15]
])
scheme_A = np.array([0.5, 0.3, 0.2])
scheme_B = np.array([0.2, 0.3, 0.5])
scheme_C = np.array([0.1, 0.2, 0.7])
#1
weight_matrix=np.array([scheme_A,scheme_B,scheme_C])
#2
final_scores=scores@weight_matrix.T
print(final_scores)
#3
best_schemes=np.argmax(final_scores, axis=1)
print(best_schemes)
#4
averages=final_scores.mean(axis=0)
best_scheme=np.argmax(averages)
#5
scheme_D=np.array([0.2, 0.4, 0.4])
weight_matrix=np.vstack((weight_matrix, scheme_D))