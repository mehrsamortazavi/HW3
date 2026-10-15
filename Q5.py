import numpy as np

#1
importance = np.array([3, 8, 1, 9, 4, 7])
method1 = importance.reshape(6,1)
method2 = importance[:,np.newaxis]
print(method1.shape)  
print(method2.shape) 
#2
model_out=np.array([[[0.9]]])
print(model_out[0,0,0])   #اسکالر
print(model_out.item())  #float
#3
notes=np.array([5,10,15,20,25])
pinned=notes[1:3]
pinned[0]=999
print(notes)
#4
notes= np.array([5,10, 15,20,25])
pinned=notes[1:3].copy()
pinned[0]=999
print(notes)
#5
notes=np.array([5,10,15,20,25])
subset=notes[2:4]
subset[1]=777
print(notes)