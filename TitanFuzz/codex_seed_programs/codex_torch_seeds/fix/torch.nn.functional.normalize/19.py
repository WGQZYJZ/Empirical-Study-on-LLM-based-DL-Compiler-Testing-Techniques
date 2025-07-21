'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.normalize\ntorch.nn.functional.normalize(input, p=2.0, dim=1, eps=1e-12, out=None)\n'
import torch
import numpy as np
import torch
x = torch.randn(2, 3, 4)
torch.nn.functional.normalize(x, p=2.0, dim=1, eps=1e-12, out=None)
print(x)