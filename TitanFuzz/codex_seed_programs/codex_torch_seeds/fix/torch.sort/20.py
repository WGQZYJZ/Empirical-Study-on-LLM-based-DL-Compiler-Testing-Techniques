'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print('input data:', input_data)
print('\nTask 3:')
print('torch.sort(input, dim=-1, descending=False, stable=False, *, out=None)')
print('The API torch.sort() returns a sorted tensor with the same shape as the input')
print('input tensor:', input_data)
print('sorted tensor:', torch.sort(input_data))
print('sorted tensor:', torch.sort(input_data, dim=1))
print('sorted tensor:', torch.sort(input_data, dim=1, descending=True))