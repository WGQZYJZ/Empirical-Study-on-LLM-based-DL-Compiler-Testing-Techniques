'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.orthogonal_\ntorch.nn.init.orthogonal_(tensor, gain=1)\n'
import torch
import torch.nn as nn
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = torch.randn(2, 3)
print('Input data:')
print(input_data)
print('Task 3: Call the API torch.nn.init.orthogonal_')
torch.nn.init.orthogonal_(input_data)
print('Output data:')
print(input_data)