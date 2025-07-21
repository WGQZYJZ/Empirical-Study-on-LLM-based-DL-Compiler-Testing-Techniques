'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
import torch
input_data = torch.randn(10)
print('Input data: \n', input_data)
output_data = torch.cos(input_data)
print('Output data: \n', output_data)