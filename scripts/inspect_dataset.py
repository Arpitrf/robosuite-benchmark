import h5py
import matplotlib.pyplot as plt
import numpy as np

f = h5py.File('/home/arpit/test_projects/robosuite-benchmark/log/runs/Lift-Panda-OSC-POSE-SEED1/Lift_Panda_OSC_POSE_SEED1_2023_09_17_12_15_42_0000--s-0/replay_buffer.hdf5') 
# print(f.keys())
img = np.array(f['000000269_step228']['observations'])[:-32].reshape(256,256,3).astype(np.int64)
print(img[0,0,0])
# plt.imshow(img)
# plt.show()