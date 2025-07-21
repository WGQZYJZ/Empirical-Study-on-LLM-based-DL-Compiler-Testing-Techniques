'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccos\ntorch.arccos(input, *, out=None)\n'
import torch
input_data = torch.rand(4, 4)
print('input_data = \n', input_data)
output_data = torch.arccos(input_data)
print('output_data = \n', output_data)