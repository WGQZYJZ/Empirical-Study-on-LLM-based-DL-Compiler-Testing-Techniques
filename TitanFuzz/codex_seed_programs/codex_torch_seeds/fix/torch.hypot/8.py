'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hypot\ntorch.hypot(input, other, *, out=None)\n'
import torch
input_data = torch.randn(5, 5)
print('Input data: ', input_data)
output_data = torch.hypot(input_data, input_data)
print('Output data: ', output_data)