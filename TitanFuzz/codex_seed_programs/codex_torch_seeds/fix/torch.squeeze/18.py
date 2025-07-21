'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
input_data = torch.randn(2, 3, 5, 1)
print('Input data: ', input_data.shape)
output = torch.squeeze(input_data)
print('Output data: ', output.shape)