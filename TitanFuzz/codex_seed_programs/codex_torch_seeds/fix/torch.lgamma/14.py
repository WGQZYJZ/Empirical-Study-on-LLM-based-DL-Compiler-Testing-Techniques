'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lgamma\ntorch.lgamma(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print('Input data: ', input_data)
output = torch.lgamma(input_data)
print('Output: ', output)