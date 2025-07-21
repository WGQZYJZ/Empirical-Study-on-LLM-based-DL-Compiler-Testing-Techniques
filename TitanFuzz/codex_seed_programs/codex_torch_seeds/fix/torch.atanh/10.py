'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atanh\ntorch.atanh(input, *, out=None)\n'
import torch
input_data = torch.randn(4, 4)
print('input_data: ', input_data)
output = torch.atanh(input_data)
print('Output: ', output)