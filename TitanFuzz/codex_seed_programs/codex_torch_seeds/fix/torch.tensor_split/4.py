'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
print('Task 1: import PyTorch')
print('\nTask 2: Generate input data')
x = torch.randn(4, 6)
print('Input data: ', x)
print('\nTask 3: Call the API torch.tensor_split')
print('torch.tensor_split(input, indices_or_sections, dim=0)')
y = torch.tensor_split(x, 3, dim=1)
print('Output: ', y)
z = torch.tensor_split(x, [1, 2, 3], dim=1)
print('Output: ', z)