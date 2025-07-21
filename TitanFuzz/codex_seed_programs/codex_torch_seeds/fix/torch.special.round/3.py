'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.round\ntorch.special.round(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3)
print('Input data: ', input_data)
output_data = torch.special.round(input_data)
print('Output data: ', output_data)