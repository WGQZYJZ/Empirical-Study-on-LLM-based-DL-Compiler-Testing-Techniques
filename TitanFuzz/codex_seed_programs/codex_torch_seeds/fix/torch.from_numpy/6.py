'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
input_data = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
torch_data = torch.from_numpy(input_data)
print(torch_data)
print(torch_data.type())
print(torch_data.size())
print(torch_data.shape)
print(torch_data.dim())
print(torch_data.ndimension())
print(torch_data.numel())