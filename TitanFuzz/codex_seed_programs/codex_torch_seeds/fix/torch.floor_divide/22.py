'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('input_data:', input_data)
other = torch.randn(2, 3)
print('other:', other)
output = torch.floor_divide(input_data, other)
print('output:', output)