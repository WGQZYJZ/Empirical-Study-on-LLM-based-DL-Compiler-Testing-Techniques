'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.deg2rad\ntorch.deg2rad(input, *, out=None)\n'
import torch
input_data = torch.rand(10)
output_data = torch.deg2rad(input_data)
print('Input data: ', input_data)
print('Output data: ', output_data)