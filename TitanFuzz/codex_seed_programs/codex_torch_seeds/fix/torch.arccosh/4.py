'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccosh\ntorch.arccosh(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
output_data = torch.arccosh(input_data)
print('Input data:')
print(input_data)
print('Output data:')
print(output_data)