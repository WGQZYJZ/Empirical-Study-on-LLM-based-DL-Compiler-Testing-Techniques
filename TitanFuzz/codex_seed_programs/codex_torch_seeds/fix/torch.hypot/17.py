'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hypot\ntorch.hypot(input, other, *, out=None)\n'
import torch
input_data = torch.rand(2, 3)
other_data = torch.rand(2, 3)
print('Input data: ', input_data)
print('Other data: ', other_data)
output_data = torch.hypot(input_data, other_data)
print('Output data: ', output_data)