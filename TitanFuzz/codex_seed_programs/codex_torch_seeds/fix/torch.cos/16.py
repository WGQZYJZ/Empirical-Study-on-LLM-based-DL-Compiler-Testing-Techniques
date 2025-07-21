'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
output_data = torch.cos(input_data)
print('Input data: ', input_data)
print('Output data: ', output_data)