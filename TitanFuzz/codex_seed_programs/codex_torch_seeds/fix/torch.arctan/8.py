'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctan\ntorch.arctan(input, *, out=None)\n'
import torch
x = torch.randn(4)
print(x)
y = torch.arctan(x)
print(y)