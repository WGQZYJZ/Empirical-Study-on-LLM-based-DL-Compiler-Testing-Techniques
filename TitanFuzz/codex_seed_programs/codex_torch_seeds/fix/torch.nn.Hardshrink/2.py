'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardshrink\ntorch.nn.Hardshrink(lambd=0.5)\n'
import torch
x = torch.randn(4, 4)
print(x)
import torch.nn as nn
x = torch.randn(4, 4)
print(x)
shrink = nn.Hardshrink(lambd=0.5)
y = shrink(x)
print(y)