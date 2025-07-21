'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
input_data = np.array([1, 2, 3])
input_tensor = torch.from_numpy(input_data)
print(input_tensor)
print(input_tensor.dtype)
print(input_tensor.shape)
print('\n')
input_data = np.array([1, 2, 3])
input_tensor = torch.tensor(input_data)
print(input_tensor)
print(input_tensor.dtype)
print(input_tensor.shape)
print('\n')