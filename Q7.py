import numpy as np
X_messages = np.array([
    [12, 0, 1],
    [45, 5, 8],
    [8, 0, 0],
    [30, 3, 4]
])
w = np.array([0.1, 0.8, 0.5])
b = -2.0
#1
raw_output=X_messages@w+b
print(raw_output)
#2
final_output=np.maximum(0, raw_output)
print(final_output)
#3
threshold = 3.0
labels = np.where(
    final_output >= threshold,
    "Energetic","Calm")
print(labels)