'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tan\ntorch.tan(input, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = torch.randn(1, 3)
print('input_data = ', input_data)
print('Task 3: Call the API torch.tan')
output_data = torch.tan(input_data)
print('output_data = ', output_data)