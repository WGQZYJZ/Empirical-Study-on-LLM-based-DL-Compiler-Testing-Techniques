'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acosh\ntorch.acosh(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data is: ', input_data)
output_data = torch.acosh(input_data)
print('Output data is: ', output_data)