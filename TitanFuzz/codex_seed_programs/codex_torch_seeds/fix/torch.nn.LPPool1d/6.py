'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch import nn
print('Task 1: import PyTorch')
print('PyTorch version: {}'.format(torch.__version__))
print('Task 2: Generate input data')
input = torch.randn(1, 1, 3, requires_grad=True)
print('Input: {}'.format(input))
print('Task 3: Call the API torch.nn.LPPool1d')
pooling = nn.LPPool1d(norm_type=2, kernel_size=2)
output = pooling(input)
print('Output: {}'.format(output))