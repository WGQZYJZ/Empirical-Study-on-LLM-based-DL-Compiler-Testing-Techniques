'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsinh\ntorch.arcsinh(input, *, out=None)\n'
import torch
input_data = torch.rand(2, 3, 4)
print('input_data:', input_data)
output = torch.arcsinh(input_data)
print('output:', output)