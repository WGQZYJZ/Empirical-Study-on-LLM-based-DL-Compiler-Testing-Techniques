'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.remainder\ntorch.remainder(input, other, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
other = torch.randn(2, 3)
print('Input data: \n', input_data)
print('Other: \n', other)
print('Output data: \n', torch.remainder(input_data, other))