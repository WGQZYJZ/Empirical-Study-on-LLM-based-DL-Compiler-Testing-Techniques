'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.constant_\ntorch.nn.init.constant_(tensor, val)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_tensor = torch.tensor(input_data, dtype=torch.float32)
print('Input tensor: ', input_tensor)
print('Task 3: Call the API torch.nn.init.constant_')
torch.nn.init.constant_(input_tensor, val=10)
print('Output tensor: ', input_tensor)