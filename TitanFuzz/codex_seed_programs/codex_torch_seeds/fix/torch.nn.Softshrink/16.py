'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softshrink\ntorch.nn.Softshrink(lambd=0.5)\n'
import torch
import torch.nn as nn
x = torch.randn(1, 3)
softshrink = nn.Softshrink(lambd=0.5)
y = softshrink(x)
print(y)