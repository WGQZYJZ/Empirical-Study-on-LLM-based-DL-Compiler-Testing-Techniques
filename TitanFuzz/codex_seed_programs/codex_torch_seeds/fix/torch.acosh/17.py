'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acosh\ntorch.acosh(input, *, out=None)\n'
import torch
import torch
input_data = torch.randn(5, 3)
print('Input data: ', input_data)
print('Result: ', torch.acosh(input_data))