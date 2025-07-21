'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor\ntorch.floor(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 2)
print('Input data: ', input_data)
output = torch.floor(input_data)
print('Output: ', output)