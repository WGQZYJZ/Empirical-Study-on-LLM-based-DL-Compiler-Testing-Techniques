'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i0\ntorch.special.i0(input, *, out=None)\n'
import torch
in_data = torch.randn(6, 3)
print('Input data: ', in_data)
out_data = torch.special.i0(in_data)
print('Output data: ', out_data)