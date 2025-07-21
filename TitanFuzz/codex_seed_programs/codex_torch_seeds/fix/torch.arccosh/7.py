'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccosh\ntorch.arccosh(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print('Input data: ', input_data)
output = torch.arccosh(input_data)
print('Output: ', output)