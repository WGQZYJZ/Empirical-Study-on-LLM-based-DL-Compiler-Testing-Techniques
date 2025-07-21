'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
input_data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
input_data_tensor = torch.from_numpy(input_data)
print('input_data_tensor = \n', input_data_tensor)
print('input_data_tensor.shape = ', input_data_tensor.shape)
print('input_data_tensor.dtype = ', input_data_tensor.dtype)
input_data_tensor = torch.tensor(input_data)
print('input_data_tensor = \n', input_data_tensor)
print('input_data_tensor.shape = ', input_data_tensor.shape)