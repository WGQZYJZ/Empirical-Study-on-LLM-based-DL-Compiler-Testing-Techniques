'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummin\ntorch.cummin(input, dim, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print('Input data: \n', input_data)
cummin_data = torch.cummin(input_data, dim=1)
print('cummin data: \n', cummin_data)