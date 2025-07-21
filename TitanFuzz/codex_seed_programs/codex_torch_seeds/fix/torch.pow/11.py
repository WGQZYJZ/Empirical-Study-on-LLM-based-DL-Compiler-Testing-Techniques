'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pow\ntorch.pow(input, exponent, *, out=None)\n'
import torch
input_data = torch.rand(2, 2, requires_grad=True)
print('Input data: ', input_data)
output_data = torch.pow(input_data, 3)
print('Output data: ', output_data)