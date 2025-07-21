'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsinh\ntorch.arcsinh(input, *, out=None)\n'
import torch
in_data = torch.randn(5)
print('Input Data: ', in_data)
out_data = torch.arcsinh(in_data)
print('Output Data: ', out_data)