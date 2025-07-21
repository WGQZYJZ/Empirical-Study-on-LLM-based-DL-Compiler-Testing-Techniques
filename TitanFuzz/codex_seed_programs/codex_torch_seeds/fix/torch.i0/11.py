'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.i0\ntorch.i0(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print('Input data: ', input_data)
output_data = torch.i0(input_data)
print('Output data: ', output_data)