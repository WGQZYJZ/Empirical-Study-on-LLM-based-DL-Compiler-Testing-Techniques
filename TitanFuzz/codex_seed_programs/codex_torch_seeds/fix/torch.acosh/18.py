'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acosh\ntorch.acosh(input, *, out=None)\n'
import torch
import numpy as np
import torch
input_data = np.array([1.0, 1.5, 2.0, 2.5])
input_data_tensor = torch.tensor(input_data)
output_data_tensor = torch.acosh(input_data_tensor)
print('Input data: ', input_data_tensor)
print('Output data: ', output_data_tensor)