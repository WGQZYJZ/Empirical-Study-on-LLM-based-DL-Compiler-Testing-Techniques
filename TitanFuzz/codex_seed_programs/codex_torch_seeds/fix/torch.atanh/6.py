'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atanh\ntorch.atanh(input, *, out=None)\n'
import torch
import numpy as np
x = torch.randn(2, 3)
print(x)
y = torch.atanh(x)
print(y)