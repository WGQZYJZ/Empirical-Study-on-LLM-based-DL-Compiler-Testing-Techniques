'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cosh\ntorch.cosh(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
output_data = torch.cosh(input_data)
print('Input data: ', input_data)
print('Output data: ', output_data)