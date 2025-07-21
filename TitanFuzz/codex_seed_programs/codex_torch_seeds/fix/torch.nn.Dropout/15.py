'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
x = torch.randn(1, 5, requires_grad=True)
dropout = nn.Dropout(p=0.5, inplace=False)
y = dropout(x)
print('x: ', x)
print('y: ', y)