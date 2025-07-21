'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccosh\ntorch.arccosh(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
print('Input data is: ', input_data)
output = torch.arccosh(input_data)
print('The output is: ', output)