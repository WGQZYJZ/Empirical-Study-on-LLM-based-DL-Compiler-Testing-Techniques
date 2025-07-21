'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccosh\ntorch.arccosh(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print('input data = ', input_data)
output_data = torch.arccosh(input_data)
print('output data = ', output_data)
torch.arccosh_(input_data)
print('input data after inplace operation = ', input_data)