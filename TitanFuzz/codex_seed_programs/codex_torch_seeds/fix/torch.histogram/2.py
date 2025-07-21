'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.histogram\ntorch.histogram(input, bins, *, range=None, weight=None, density=False, out=None)\n'
import torch
import numpy as np
x = torch.randn(1000)
hist = torch.histogram(x, bins=100)
print(hist)