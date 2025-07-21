'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
import torch
input_data = torch.randn(3, 5)
other_data = torch.randn(3, 5)
output = torch.floor_divide(input_data, other_data)
print('Output: ', output)
print('Shape of input: ', input_data.shape)
print('Shape of output: ', output.shape)