'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctanh\ntorch.arctanh(input, *, out=None)\n'
import torch
import math
import torch
input_data = torch.rand(10, 10)
output = torch.arctanh(input_data)
print('Input data: \n', input_data)
print('Output data: \n', output)