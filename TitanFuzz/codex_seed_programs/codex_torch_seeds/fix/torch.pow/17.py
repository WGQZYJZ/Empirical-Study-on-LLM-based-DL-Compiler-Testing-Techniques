'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pow\ntorch.pow(input, exponent, *, out=None)\n'
import torch
input_data = torch.arange(1, 10, dtype=torch.float)
print('input_data: ', input_data)
output_data = torch.pow(input_data, 2)
print('output_data: ', output_data)