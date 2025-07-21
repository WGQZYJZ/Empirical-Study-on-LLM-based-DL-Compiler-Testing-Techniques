'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.igammac\ntorch.igammac(input, other, *, out=None)\n'
import torch
import numpy as np
x = torch.tensor(np.random.randn(10, 10), dtype=torch.float32)
other = torch.tensor(np.random.randn(10, 10), dtype=torch.float32)
y = torch.igammac(x, other)
print(y)