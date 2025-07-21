'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
import torch
x = torch.randn(4)
print(x)
y = torch.cos(x)
print(y)