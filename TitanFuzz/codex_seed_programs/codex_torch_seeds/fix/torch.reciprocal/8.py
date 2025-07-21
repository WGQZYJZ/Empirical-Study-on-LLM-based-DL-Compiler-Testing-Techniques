'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reciprocal\ntorch.reciprocal(input, *, out=None)\n'
import torch
x = torch.randn(3, 3)
print(x)
y = torch.reciprocal(x)
print(y)