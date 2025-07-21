'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asinh\ntorch.asinh(input, *, out=None)\n'
import torch
in_data = torch.randn(5)
print('Input data: ', in_data)
out_data = torch.asinh(in_data)
print('Output data: ', out_data)