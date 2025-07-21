'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.rand(1, 3)
print('input data: \n', input_data)
output = torch.min(input_data, 1)
print('output: \n', output)
output = torch.min(input_data, 0)
print('output: \n', output)