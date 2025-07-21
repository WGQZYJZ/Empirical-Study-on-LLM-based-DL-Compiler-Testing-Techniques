'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_uniform_\ntorch.nn.init.xavier_uniform_(tensor, gain=1.0)\n'
import torch
import torch.nn as nn
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
tensor = torch.randn(3, 5)
print('Input tensor: \n', tensor)
print('Task 3: Call the API torch.nn.init.xavier_uniform_')
print('torch.nn.init.xavier_uniform_(tensor, gain=1.0)')
nn.init.xavier_uniform_(tensor, gain=1.0)
print('Output tensor: \n', tensor)