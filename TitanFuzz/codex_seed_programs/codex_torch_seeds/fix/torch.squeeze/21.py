'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
input_data = torch.randn(2, 1, 2, 1, 2)
print('input_data.shape: ', input_data.shape)
squeeze_data = torch.squeeze(input_data)
print('squeeze_data.shape: ', squeeze_data.shape)