'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isposinf\ntorch.isposinf(input, *, out=None)\n'
import torch
a = torch.randn(4, 4)
print(a)
b = torch.isposinf(a)
print(b)