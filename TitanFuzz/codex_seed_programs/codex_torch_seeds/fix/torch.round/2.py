'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
x = torch.randn(3, 4)
print(x)
y = torch.round(x)
print(y)