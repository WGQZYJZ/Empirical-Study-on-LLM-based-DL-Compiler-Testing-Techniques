'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acos\ntorch.acos(input, *, out=None)\n'
import torch
import math
input_data = torch.rand(1, dtype=torch.float64)
result = torch.acos(input_data)
print('torch.acos(input_data) = ', result)
import numpy as np
input_data_numpy = input_data.numpy()
result_numpy = np.arccos(input_data_numpy)
print('np.arccos(input_data_numpy) = ', result_numpy)