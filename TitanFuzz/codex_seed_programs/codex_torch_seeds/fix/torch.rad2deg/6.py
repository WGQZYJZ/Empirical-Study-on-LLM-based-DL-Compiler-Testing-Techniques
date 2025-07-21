'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rad2deg\ntorch.rad2deg(input, *, out=None)\n'
import torch
input_data = torch.randn(100, 100)
output = torch.rad2deg(input_data)
print('The input data: ', input_data)
print('The output data: ', output)