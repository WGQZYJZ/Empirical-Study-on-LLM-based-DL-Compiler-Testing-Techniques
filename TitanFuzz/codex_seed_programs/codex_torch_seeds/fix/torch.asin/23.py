'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asin\ntorch.asin(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print('Input data: ', input_data)
output_data = torch.asin(input_data)
print('Output data: ', output_data)