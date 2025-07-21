'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctan\ntorch.arctan(input, *, out=None)\n'
import torch
input_data = torch.rand(5)
print('Input data: ', input_data)
output_data = torch.arctan(input_data)
print('Output data: ', output_data)