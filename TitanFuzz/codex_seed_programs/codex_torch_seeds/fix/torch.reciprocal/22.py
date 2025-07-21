'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reciprocal\ntorch.reciprocal(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
y = torch.reciprocal(x)
print(x)
print(y)