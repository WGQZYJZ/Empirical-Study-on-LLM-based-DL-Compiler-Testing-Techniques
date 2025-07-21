'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.negative\ntorch.negative(input, *, out=None)\n'
import torch
input_data = torch.rand(3, 3)
print('Input data: ', input_data)
output = torch.negative(input_data)
print('Output data: ', output)