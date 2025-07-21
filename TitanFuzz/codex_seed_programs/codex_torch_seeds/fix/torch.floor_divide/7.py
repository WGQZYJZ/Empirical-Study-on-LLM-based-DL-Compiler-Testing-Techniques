'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
input_data = torch.randn(10, 10)
other_data = torch.randn(10, 10)
output = torch.floor_divide(input_data, other_data)
print('Input data: ', input_data)
print('Other data: ', other_data)
print('Output data: ', output)