'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GELU\ntorch.nn.GELU()\n'
import torch
import torch.nn as nn
import torch
x = torch.randn(4, 4)
y = nn.GELU()(x)
print('Input data: ', x)
print('Output data: ', y)