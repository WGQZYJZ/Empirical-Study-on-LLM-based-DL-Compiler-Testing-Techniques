'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmin\ntorch.argmin(input, dim=None, keepdim=False)\n'
import torch
input_data = torch.randn(3, 4)
print('input data:')
print(input_data)
argmin_data = torch.argmin(input_data, dim=1)
print('argmin data:')
print(argmin_data)