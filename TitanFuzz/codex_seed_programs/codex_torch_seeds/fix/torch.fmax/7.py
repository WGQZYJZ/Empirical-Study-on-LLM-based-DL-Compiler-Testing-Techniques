'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
input_data = torch.rand(4, 3)
print('Input data: ', input_data)
output_data = torch.fmax(input_data, torch.ones(4, 3))
print('Output data: ', output_data)