'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
input_data = torch.randn(2, 1, 2, 1, 2)
print('Input data: ', input_data)
output = torch.squeeze(input_data)
print('Output: ', output)
output = torch.squeeze(input_data, 0)
print('Output: ', output)
output = torch.squeeze(input_data, 1)
print('Output: ', output)