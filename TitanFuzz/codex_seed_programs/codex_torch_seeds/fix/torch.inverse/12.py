'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inverse\ntorch.inverse(input, *, out=None)\n'
import torch
import numpy as np
x = torch.randn(3, 3)
print(x)
y = torch.inverse(x)
print(y)
print(torch.mm(x, y))