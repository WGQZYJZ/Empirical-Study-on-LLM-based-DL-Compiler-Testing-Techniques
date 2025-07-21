'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctanh\ntorch.arctanh(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
print(input_data)
output = torch.arctanh(input_data)
print(output)