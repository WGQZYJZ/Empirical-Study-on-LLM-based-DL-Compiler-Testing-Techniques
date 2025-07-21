'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.expm1\ntorch.expm1(input, *, out=None)\n'
import torch
import numpy as np
input_data = np.random.rand(3, 4)
input_data = torch.tensor(input_data)
print('input_data = ', input_data)
output = torch.expm1(input_data)
print('output = ', output)