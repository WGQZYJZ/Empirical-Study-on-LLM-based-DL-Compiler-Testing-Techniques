'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sigmoid\ntorch.sigmoid(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('input data: ', input_data)
output_data = torch.sigmoid(input_data)
print('output data: ', output_data)