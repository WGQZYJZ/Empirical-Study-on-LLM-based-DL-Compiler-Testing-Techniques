'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctanh\ntorch.arctanh(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print(input_data)
print(torch.arctanh(input_data))
print(torch.atanh_(input_data))
print(input_data)