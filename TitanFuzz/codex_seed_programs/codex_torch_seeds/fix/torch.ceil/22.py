'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ceil\ntorch.ceil(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('input data: ', input_data)
output = torch.ceil(input_data)
print('output data: ', output)