'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
print('\nnumpy array:', np_data, '\ntorch tensor:', torch_data)
torch2array = torch_data.numpy()
print('\ntorch tensor:', torch_data, '\ntorch array:', torch2array)