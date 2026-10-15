import numpy as np
weather_data = np.random.randn(2, 8, 4) * 5 + 20
#1
day2=weather_data[1]
day2_transposed=day2.T

yek_bod=weather_data.reshape(-1)
print(yek_bod.shape)

day3=np.random.randn(8, 4)
day3=day3[np.newaxis, :, :]
weather_data=np.concatenate((weather_data, day3),axis=0)
print(weather_data.shape)
