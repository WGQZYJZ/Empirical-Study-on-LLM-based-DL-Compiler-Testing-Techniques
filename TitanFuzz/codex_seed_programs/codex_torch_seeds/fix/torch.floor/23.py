'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor\ntorch.floor(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print('input_data: ', input_data)
output_data = torch.floor(input_data)
print('output_data: ', output_data)