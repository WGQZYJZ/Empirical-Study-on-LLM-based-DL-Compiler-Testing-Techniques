'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atanh\ntorch.atanh(input, *, out=None)\n'
import torch
input_data = torch.randn(10, 10)
print('Input data: ', input_data)
output_data = torch.atanh(input_data)
print('Output data: ', output_data)