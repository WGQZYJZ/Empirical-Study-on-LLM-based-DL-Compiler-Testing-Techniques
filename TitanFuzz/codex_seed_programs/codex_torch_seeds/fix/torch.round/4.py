'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input_data = torch.randn(5)
output_data = torch.round(input_data)
print('input data: ', input_data)
print('output data: ', output_data)