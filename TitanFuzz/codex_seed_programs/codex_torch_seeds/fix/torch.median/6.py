'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.median\ntorch.median(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = torch.randn(1, 3, 3, 3)
print('Input data: ', input_data)
print('Task 3: Call the API torch.median')
output = torch.median(input_data)
print('Output: ', output)