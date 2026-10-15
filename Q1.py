import numpy as np
gym_data = np.array([
[28, 75, 175, 4],
[34, 68, 168, 3],
[45, 82, 180, 2],
[22, 58, 162, 5],
[38, 90, 0, 1],
[29, 65, 170, 0]
])
member_names = np.array(["Ali", "Sara", "Reza", "Neda", "Hassan",
"Maryam"])
#1
gym_data[4,2]=190
gym_data[5,3]=3
print(gym_data)
#2
new=gym_data[:5, 1:4]
print(new)
#3
bmi = new[:,0]/(new[:,1]/100)** 2
score=0.1*bmi+2*new[:,2]
new=np.column_stack((new, score))
#4
best_member= member_names[np.argmax(score)]
print(best_member)
#5   
sessions=gym_data[:,3]
z_scores=(sessions-sessions.mean())/sessions.std()
unusual_member = member_names[np.argmax(np.abs(z_scores))]
print(unusual_member)