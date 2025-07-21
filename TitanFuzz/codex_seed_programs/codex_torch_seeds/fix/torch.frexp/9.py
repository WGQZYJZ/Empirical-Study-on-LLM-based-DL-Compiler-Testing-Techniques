'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frexp\ntorch.frexp(input, *, out=None)\n'
import torch
x = torch.randn(1)
print(x)
y = torch.frexp(x)
print(y)