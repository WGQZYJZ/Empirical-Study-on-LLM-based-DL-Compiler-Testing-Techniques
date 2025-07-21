'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Flatten\ntorch.nn.Flatten(start_dim=1, end_dim=-1)\n'
import torch
from torch.nn import Flatten
input_data = torch.randn(1, 3, 4, 5)
print('Input data shape: ', input_data.shape)
flatten = Flatten(start_dim=1, end_dim=(- 1))
output = flatten(input_data)
print('Output shape: ', output.shape)
print('Output data: ', output)