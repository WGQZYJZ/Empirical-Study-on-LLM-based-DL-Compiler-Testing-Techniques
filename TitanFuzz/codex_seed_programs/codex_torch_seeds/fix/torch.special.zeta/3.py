'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.zeta\ntorch.special.zeta(input, other, *, out=None)\n'
import torch
import numpy as np
x = torch.randn(3, 3)
y = torch.randn(3, 3)
out = torch.special.zeta(x, y)
print(out)