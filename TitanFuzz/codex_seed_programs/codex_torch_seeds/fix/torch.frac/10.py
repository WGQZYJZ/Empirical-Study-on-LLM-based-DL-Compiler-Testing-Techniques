'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frac\ntorch.frac(input, *, out=None)\n'
import torch
input_data = torch.rand(5, 3)
output_data = torch.frac(input_data)
print('input data: ', input_data)
print('output data: ', output_data)