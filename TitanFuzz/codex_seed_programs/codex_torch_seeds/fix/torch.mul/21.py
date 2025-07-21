'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
import torch
input_data = torch.rand(2, 3)
print('Input data: ', input_data)
output_data = torch.mul(input_data, input_data)
print('Output data: ', output_data)