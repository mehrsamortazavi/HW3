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
#3
bmi_list=[]
def BMI(gym_data):
    for i in gym_data:
        bmi=i[1]/((i[2]/100)**2)
        bmi_list.append(bmi)
    return bmi_list
scores_list=[]
def score(gym_data, member_names, bmi_list):
    w1=1
    w2=1
    for i in range(len(gym_data)):
                score=((w1*gym_data[i, 3]))+(w2*bmi_list[i])
                scores_list.append(score)
                print(f" score of {member_names[i]} is {score:.1f}")
    return score
BMI(gym_data)
score(gym_data, member_names, bmi_list)
#4
def maxii(scores_list, member_names):
    maximum=max(scores_list)
    i=scores_list.index(maximum)
    print(f"{member_names[i]} has maximum score of {maximum}")
maxii(scores_list, member_names)
#5

jalasat=gym_data[:, 3]
mean_jalasat=np.mean(jalasat)
std_jalasat=np.std(jalasat)
differences = np.abs(jalasat - mean_jalasat)
index = np.argmax(differences)
print(f"Member:{member_names[index]}")
print(f"tedad jalasat: {jalasat[index]}")
print(f"d from mean: {differences[index]:.2f}")
print(f"enheraf meyar: {std_jalasat:.2f}")