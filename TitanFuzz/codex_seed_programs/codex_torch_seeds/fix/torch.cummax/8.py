'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummax\ntorch.cummax(input, dim, *, out=None)\n'
import torch
input_data = torch.rand(2, 3)
print('Input data: ', input_data)
output_data = torch.cummax(input_data, dim=0)
print('Output data: ', output_data)