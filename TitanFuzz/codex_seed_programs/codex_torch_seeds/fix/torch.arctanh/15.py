'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctanh\ntorch.arctanh(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 3, requires_grad=True)
output_data = torch.arctanh(input_data)
print('Input data:\n', input_data)
print('Output data:\n', output_data)