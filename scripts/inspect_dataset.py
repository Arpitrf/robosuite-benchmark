import h5py
import matplotlib.pyplot as plt
import numpy as np

f = h5py.File('/home/arpit/test_projects/robosuite-benchmark/log/runs/Lift-Panda-OSC-POSE-SEED1/Lift_Panda_OSC_POSE_SEED1_2023_09_17_16_52_48_0000--s-0/replay_buffer.hdf5') 
print(np.array(f['000000218_step76']['rewards']))
counter = 0
for k in f.keys():
    if np.array(f[k]['rewards'])[0] == 1.0:
        counter += 1 

print("Total transitions with 1 reward: ", counter)
# img = np.array(f['000000269_step228']['observations'])[:-32].reshape(256,256,3).astype(np.int64)
# print(img[0,0,0])
# plt.imshow(img)
# plt.show()